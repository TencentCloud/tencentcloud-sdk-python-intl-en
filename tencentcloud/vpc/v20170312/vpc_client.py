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
from tencentcloud.vpc.v20170312 import models


class VpcClient(AbstractClient):
    _apiVersion = '2017-03-12'
    _endpoint = 'vpc.intl.tencentcloudapi.com'
    _service = 'vpc'


    def AcceptAttachCcnInstances(self, request):
        """This API (AcceptAttachCcnInstances) is used to associate instances across accounts. Cloud Connect Network (CCN) owners accept and agree to the operations.

        :param request: Request instance for AcceptAttachCcnInstances.
        :type request: :class:`tencentcloud.vpc.v20170312.models.AcceptAttachCcnInstancesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.AcceptAttachCcnInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AcceptAttachCcnInstances", params, headers=headers)
            response = json.loads(body)
            model = models.AcceptAttachCcnInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AddBandwidthPackageResources(self, request):
        """This API is used to add resources to a bandwidth package, including [Elastic IP](https://intl.cloud.tencent.com/document/product/213/1941?from_cn_redirect=1), [Cloud Load Balancer](https://intl.cloud.tencent.com/document/product/214/517?from_cn_redirect=1), and so on.

        :param request: Request instance for AddBandwidthPackageResources.
        :type request: :class:`tencentcloud.vpc.v20170312.models.AddBandwidthPackageResourcesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.AddBandwidthPackageResourcesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddBandwidthPackageResources", params, headers=headers)
            response = json.loads(body)
            model = models.AddBandwidthPackageResourcesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AddTemplateMember(self, request):
        """This API is used to add a parameter template of the IP address, protocol port, IP address group, or protocol port group type.

        :param request: Request instance for AddTemplateMember.
        :type request: :class:`tencentcloud.vpc.v20170312.models.AddTemplateMemberRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.AddTemplateMemberResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddTemplateMember", params, headers=headers)
            response = json.loads(body)
            model = models.AddTemplateMemberResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AdjustPublicAddress(self, request):
        """This API is used to change the public IP of a CVM or the EIP of the associated bandwidth package.

        :param request: Request instance for AdjustPublicAddress.
        :type request: :class:`tencentcloud.vpc.v20170312.models.AdjustPublicAddressRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.AdjustPublicAddressResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AdjustPublicAddress", params, headers=headers)
            response = json.loads(body)
            model = models.AdjustPublicAddressResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AllocateAddresses(self, request):
        """This API is used to apply for one or more [Elastic IP Addresses](https://intl.cloud.tencent.com/document/product/213/1941?from_cn_redirect=1) (EIPs for short).
        * An EIP is a static IP address that is dedicated for dynamic cloud computing. You can quickly re-map an EIP to another instance under your account to protect against instance failures.
        * Your EIP is associated with your Tencent Cloud account rather than an instance. It remains associated with your Tencent Cloud account until you choose to explicitly release it or your account is in arrears for more than 24 hours.
        * The maximum number of EIPs that can be applied for a Tencent Cloud account in each region is restricted. For more information, see [EIP Product Introduction](https://intl.cloud.tencent.com/document/product/213/5733?from_cn_redirect=1). You can get the quota information through the DescribeAddressQuota API.

        :param request: Request instance for AllocateAddresses.
        :type request: :class:`tencentcloud.vpc.v20170312.models.AllocateAddressesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.AllocateAddressesResponse`

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


    def AllocateIPv6Addresses(self, request):
        """This API is used to apply for one or more Elastic IPv6 (EIPv6) instances.

        - EIPv6 is a fixed public IPv6 address that can be independently applied for and held in a Tencent Cloud region, providing a consistent product experience with Elastic IPv4.
        - You can quickly bind an EIPv6 instance to the private IPv6 address of a cloud resource, so as to quickly enable IPv6 public bandwidth for the cloud resource.
        - You can also bind an EIPv6 instance to other cloud resources as needed, so as to shield instance failures.

        :param request: Request instance for AllocateIPv6Addresses.
        :type request: :class:`tencentcloud.vpc.v20170312.models.AllocateIPv6AddressesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.AllocateIPv6AddressesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AllocateIPv6Addresses", params, headers=headers)
            response = json.loads(body)
            model = models.AllocateIPv6AddressesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AllocateIp6AddressesBandwidth(self, request):
        """This API is used to allocate IPv6 public network bandwidth for classic elastic public IPv6 addresses.

        - Classic elastic public IPv6 addresses only have the private network communication capability by default. They can have the IPv6 public network communication capability and be displayed in the list of Classic Elastic Public IPv6 only after IPv6 public network bandwidth is allocated in the console or by calling this API.
        - You can allocate public network bandwidth for one or multiple Classic elastic public IPv6 addresses each time.

        :param request: Request instance for AllocateIp6AddressesBandwidth.
        :type request: :class:`tencentcloud.vpc.v20170312.models.AllocateIp6AddressesBandwidthRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.AllocateIp6AddressesBandwidthResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AllocateIp6AddressesBandwidth", params, headers=headers)
            response = json.loads(body)
            model = models.AllocateIp6AddressesBandwidthResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AssignIpv6Addresses(self, request):
        """This API is used to apply for an IPv6 address for the ENI. <br />
        This API is completed asynchronously. If you need to query the execution result of an async task, please use the `RequestId` returned by this API to poll the `DescribeVpcTaskResult` API.
        * The number of IPs bound with an ENI is limited. For more information, see <a href="/document/product/576/18527">ENI Use Limits</a>.
        * You can apply for a specified IPv6 address. Currently, the IPv6 address can only be used as a secondary IP, instead of the primary IP.
        * The address must be an idle IP in the subnet to which the ENI belongs.
        * When applying for one or more secondary IPv6 addresses for an ENI, the API will return the specified number of secondary IPv6 addresses in the subnet range where the ENI is located.

        :param request: Request instance for AssignIpv6Addresses.
        :type request: :class:`tencentcloud.vpc.v20170312.models.AssignIpv6AddressesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.AssignIpv6AddressesResponse`

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


    def AssignIpv6CidrBlock(self, request):
        """This API is used to assign IPv6 ranges.
        * To use this API, you must already have a VPC instance. If you do not have a VPC instance yet, use the <a href="https://intl.cloud.tencent.com/document/api/215/15774?from_cn_redirect=1" title="CreateVpc" target="_blank">CreateVpc</a> API to create one.
        * Each VPC can apply for only one IPv6 range.

        :param request: Request instance for AssignIpv6CidrBlock.
        :type request: :class:`tencentcloud.vpc.v20170312.models.AssignIpv6CidrBlockRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.AssignIpv6CidrBlockResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AssignIpv6CidrBlock", params, headers=headers)
            response = json.loads(body)
            model = models.AssignIpv6CidrBlockResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AssignIpv6SubnetCidrBlock(self, request):
        """This API (AssignIpv6SubnetCidrBlock) is used to assign IPv6 subnet IP ranges.
        * To assign an `IPv6` IP range to a subnet, the `VPC` that the subnet belongs to should have obtained the `IPv6` IP range. If this has not been assigned, use the `AssignIpv6CidrBlock` API to assign an `IPv6` IP range to the `VPC` to which the subnet belongs. Otherwise, the `IPv6` subnet IP range cannot be assigned.
        * Each subnet can only be assigned one IPv6 IP range.

        :param request: Request instance for AssignIpv6SubnetCidrBlock.
        :type request: :class:`tencentcloud.vpc.v20170312.models.AssignIpv6SubnetCidrBlockRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.AssignIpv6SubnetCidrBlockResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AssignIpv6SubnetCidrBlock", params, headers=headers)
            response = json.loads(body)
            model = models.AssignIpv6SubnetCidrBlockResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AssignPrivateIpAddresses(self, request):
        """This API is used to apply for private IPs for an ENI.
        * An ENI can only be bound with a limited number of IP addresses. For more information about resource limits, see <a href="/document/product/576/18527">ENI Use Limits</a>.
        * You can apply for a specified private IP. It cannot be a primary IP because the primary IP already exists and cannot be modified. The private IP address must be an idle IP in the subnet to which the ENI belongs.
        * You can apply for more than one secondary private IP on the ENI. The API will return the specified number of secondary private IPs in the subnet IP range.
        >?This API is async. You can call the [`DescribeVpcTaskResult`](https://intl.cloud.tencent.com/document/api/215/59037?from_cn_redirect=1) API to query the task result. When the task is completed, you can continue other tasks.
        >

        :param request: Request instance for AssignPrivateIpAddresses.
        :type request: :class:`tencentcloud.vpc.v20170312.models.AssignPrivateIpAddressesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.AssignPrivateIpAddressesResponse`

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
        """This API is used to bind an [Elastic IP](https://intl.cloud.tencent.com/document/product/213/1941?from_cn_redirect=1) (EIP for short) to the specified private IP of an instance or ENI.
        * Binding an EIP to a CVM instance is actually binding the EIP to the primary private IP of the primary ENI on the CVM instance.
        * When an EIP is bound, the public IP previously bound to the CVM instance will be unbound and released automatically.
        * To bind another EIP to the private IP of the specified ENI, you must first unbind the EIP.
        * To bind an EIP to a NAT Gateway, use the API [AssociateNatGatewayAddress](https://intl.cloud.tencent.com/document/product/215/36722?from_cn_redirect=1).
        * An EIP cannot be bound if it’s overdue or blocked
        * Only EIP in the `UNBIND` status can be bound.

        :param request: Request instance for AssociateAddress.
        :type request: :class:`tencentcloud.vpc.v20170312.models.AssociateAddressRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.AssociateAddressResponse`

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


    def AssociateDirectConnectGatewayNatGateway(self, request):
        """This API is used to bind a direct connect gateway with a NAT gateway,  and direct its default route to the NAT Gateway.

        :param request: Request instance for AssociateDirectConnectGatewayNatGateway.
        :type request: :class:`tencentcloud.vpc.v20170312.models.AssociateDirectConnectGatewayNatGatewayRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.AssociateDirectConnectGatewayNatGatewayResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AssociateDirectConnectGatewayNatGateway", params, headers=headers)
            response = json.loads(body)
            model = models.AssociateDirectConnectGatewayNatGatewayResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AssociateIPv6Address(self, request):
        """This API is used to bind an EIPv6 instance to the private IPv6 address configured on the CVM or ENI.

        - Binding an EIPv6 to the CVM essentially indicates binding the EIPv6 to the private IPv6 address configured on the ENI of the CVM.
        - Before binding an EIPv6 to the private IPv6 of a specified ENI, ensure that the private IPv6 address is unbound before the binding operation is performed.

        :param request: Request instance for AssociateIPv6Address.
        :type request: :class:`tencentcloud.vpc.v20170312.models.AssociateIPv6AddressRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.AssociateIPv6AddressResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AssociateIPv6Address", params, headers=headers)
            response = json.loads(body)
            model = models.AssociateIPv6AddressResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AssociateNatGatewayAddress(self, request):
        """This API is used to bind an EIP to a NAT gateway.

        :param request: Request instance for AssociateNatGatewayAddress.
        :type request: :class:`tencentcloud.vpc.v20170312.models.AssociateNatGatewayAddressRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.AssociateNatGatewayAddressResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AssociateNatGatewayAddress", params, headers=headers)
            response = json.loads(body)
            model = models.AssociateNatGatewayAddressResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AssociateNetworkAclSubnets(self, request):
        """This API is used to associate a network ACL with subnets in a VPC instance.

        :param request: Request instance for AssociateNetworkAclSubnets.
        :type request: :class:`tencentcloud.vpc.v20170312.models.AssociateNetworkAclSubnetsRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.AssociateNetworkAclSubnetsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AssociateNetworkAclSubnets", params, headers=headers)
            response = json.loads(body)
            model = models.AssociateNetworkAclSubnetsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AssociateNetworkInterfaceSecurityGroups(self, request):
        """This API (AssociateNetworkInterfaceSecurityGroups) is used to attach a security group to an ENI.

        :param request: Request instance for AssociateNetworkInterfaceSecurityGroups.
        :type request: :class:`tencentcloud.vpc.v20170312.models.AssociateNetworkInterfaceSecurityGroupsRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.AssociateNetworkInterfaceSecurityGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AssociateNetworkInterfaceSecurityGroups", params, headers=headers)
            response = json.loads(body)
            model = models.AssociateNetworkInterfaceSecurityGroupsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AttachCcnInstances(self, request):
        """This API is used to add a network instance to a CCN instance. Network instances include VPCs and Direct Connect gateways. <br />
        The number of network instances that each CCN can be associated with is limited. For more information, see the product documentation. If you need to associate more instances, please submit a ticket.

        :param request: Request instance for AttachCcnInstances.
        :type request: :class:`tencentcloud.vpc.v20170312.models.AttachCcnInstancesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.AttachCcnInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AttachCcnInstances", params, headers=headers)
            response = json.loads(body)
            model = models.AttachCcnInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AttachClassicLinkVpc(self, request):
        """This API is used to create a Classiclink between a VPC instance and a classic network device.
        * The VPC instance and the classic network device must be in the same region.
        * For differences between VPC and the classic network, see <a href="https://intl.cloud.tencent.com/document/product/215/30720?from_cn_redirect=1">VPC and Classic Network</a>.
        >?This API is async. You can call the [`DescribeVpcTaskResult`](https://intl.cloud.tencent.com/document/api/215/59037?from_cn_redirect=1) API to query the task result. When the task is completed, you can continue other tasks.
        >

        :param request: Request instance for AttachClassicLinkVpc.
        :type request: :class:`tencentcloud.vpc.v20170312.models.AttachClassicLinkVpcRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.AttachClassicLinkVpcResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AttachClassicLinkVpc", params, headers=headers)
            response = json.loads(body)
            model = models.AttachClassicLinkVpcResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AttachNetworkInterface(self, request):
        """This API is used to bind an ENI to a CVM.
        * An ENI must be bound with one security group at least. To bind it, see <a href="https://intl.cloud.tencent.com/document/product/215/43132?from_cn_redirect=1">AssociateNetworkInterfaceSecurityGroups</a>.
        * One CVM can be bound with multiple ENIs, but only one can be the primary ENI. For more information about the limits, see <a href="https://intl.cloud.tencent.com/document/product/576/18527?from_cn_redirect=1">ENI Use Limits</a>.
        * An ENI can only be bound to one CVM.
        * Only the running or shutdown CVMs can be bound with ENIs. For more information about the CVM status, see <a href="https://intl.cloud.tencent.com/document/api/213/9452?from_cn_redirect=1#InstanceStatus">InstanceStatus</a> in the Data Types.
        * An ENI can only be bound to a VPC-based CVM under the same availability zone as the ENI subnet.

        This API is completed asynchronously. If you need to query the execution result of an async task, please use the `RequestId` returned by this API to poll the `DescribeVpcTaskResult` API.

        :param request: Request instance for AttachNetworkInterface.
        :type request: :class:`tencentcloud.vpc.v20170312.models.AttachNetworkInterfaceRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.AttachNetworkInterfaceResponse`

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


    def AttachSnapshotInstances(self, request):
        """This API is used to associate a snapshot policy with specified instances.

        :param request: Request instance for AttachSnapshotInstances.
        :type request: :class:`tencentcloud.vpc.v20170312.models.AttachSnapshotInstancesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.AttachSnapshotInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AttachSnapshotInstances", params, headers=headers)
            response = json.loads(body)
            model = models.AttachSnapshotInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AuditCrossBorderCompliance(self, request):
        """This API is used by the service provider to perform a compliance audit.
        * This API is only provided for service providers to audit compliance review requests received. Tencent Cloud will verify the identity of the service provider by the `APPID`.
        * The status of the review request can be changed between `APPROVED` and `DENY`.

        :param request: Request instance for AuditCrossBorderCompliance.
        :type request: :class:`tencentcloud.vpc.v20170312.models.AuditCrossBorderComplianceRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.AuditCrossBorderComplianceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AuditCrossBorderCompliance", params, headers=headers)
            response = json.loads(body)
            model = models.AuditCrossBorderComplianceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CheckAssistantCidr(self, request):
        """This API is used to check whether the secondary CIDR block conflicts with existing routes, peering connections (peer VPC CIDR blocks), and other resources.
        * Check whether the secondary CIDR block overlaps with the primary/secondary CIDR block of the current VPC.
        * Check whether the secondary CIDR block overlaps with the routing destination of the current VPC.
        * If the current VPC is used in a peering connection, check whether the secondary CIDR block overlaps with the primary/secondary CIDR block of the peer VPC.

        :param request: Request instance for CheckAssistantCidr.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CheckAssistantCidrRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CheckAssistantCidrResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CheckAssistantCidr", params, headers=headers)
            response = json.loads(body)
            model = models.CheckAssistantCidrResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CheckNetDetectState(self, request):
        """This API is used to verify the network detection status.

        :param request: Request instance for CheckNetDetectState.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CheckNetDetectStateRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CheckNetDetectStateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CheckNetDetectState", params, headers=headers)
            response = json.loads(body)
            model = models.CheckNetDetectStateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CloneSecurityGroup(self, request):
        """This API is used to create a security group with the same rule configurations as an existing security group. The cloning only copies the security group and its rules, but not the security group tags.

        :param request: Request instance for CloneSecurityGroup.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CloneSecurityGroupRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CloneSecurityGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CloneSecurityGroup", params, headers=headers)
            response = json.loads(body)
            model = models.CloneSecurityGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAddressTemplate(self, request):
        """This API is used to create an IP address template.

        :param request: Request instance for CreateAddressTemplate.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CreateAddressTemplateRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CreateAddressTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAddressTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAddressTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAddressTemplateGroup(self, request):
        """This API is used to create an IP address template group.

        :param request: Request instance for CreateAddressTemplateGroup.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CreateAddressTemplateGroupRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CreateAddressTemplateGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAddressTemplateGroup", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAddressTemplateGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAndAttachNetworkInterface(self, request):
        """This API is used to create an ENI and bind it to a CVM.
        * You can specify private IP addresses and a primary IP when creating an ENI. The specified private IP must be idle and in the same subnet as the ENI.
        * When creating an ENI, you can specify the number of private IPs that you want to apply for. The system will randomly generate private IP addresses.
        * The number of IPs bound with an ENI is limited. For more information, see <a href="/document/product/576/18527">ENI Use Limits</a>.
        * You can bind an existing security group when creating an ENI.
        * You can bind a tag when creating an ENI. The tag list in the response indicates the tags that have been successfully added.
        >?This API is async. You can call the [`DescribeVpcTaskResult`](https://intl.cloud.tencent.com/document/api/215/59037?from_cn_redirect=1) API to query the task result. When the task is completed, you can continue other tasks.
        >

        :param request: Request instance for CreateAndAttachNetworkInterface.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CreateAndAttachNetworkInterfaceRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CreateAndAttachNetworkInterfaceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAndAttachNetworkInterface", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAndAttachNetworkInterfaceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAssistantCidr(self, request):
        """This API is used to batch create secondary CIDR blocks.

        :param request: Request instance for CreateAssistantCidr.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CreateAssistantCidrRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CreateAssistantCidrResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAssistantCidr", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAssistantCidrResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateBandwidthPackage(self, request):
        """This API is used to create a [device bandwidth package](https://intl.cloud.tencent.com/document/product/684/15245?from_cn_redirect=1#bwptype) or an [IP bandwidth package](https://intl.cloud.tencent.com/document/product/684/15245?from_cn_redirect=1#bwptype).

        :param request: Request instance for CreateBandwidthPackage.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CreateBandwidthPackageRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CreateBandwidthPackageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateBandwidthPackage", params, headers=headers)
            response = json.loads(body)
            model = models.CreateBandwidthPackageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCcn(self, request):
        """This API is used to create a CCN instance.
        * You can add tags to a CCN instance upon the creation. The tags are added successfully if they are listed in the response.
        * There is a quota of CCN instances for each account. For more information, see product documentation. To increase the quota, please submit a ticket.

        :param request: Request instance for CreateCcn.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CreateCcnRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CreateCcnResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCcn", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCcnResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCustomerGateway(self, request):
        """This API (CreateCustomerGateway) is used to create customer gateways.

        :param request: Request instance for CreateCustomerGateway.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CreateCustomerGatewayRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CreateCustomerGatewayResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCustomerGateway", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCustomerGatewayResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDefaultVpc(self, request):
        """This API is used to create a VPC with default settings.

        To create a VPC with custom settings, such as VPC name, IP range, subnet IP range, and subnet availability zone, use `CreateVpc` instead.

        This API may not create a default VPC. It depends on the network attributes (`DescribeAccountAttributes`) of your account.
        * If both basic network and VPC are supported, the returned `VpcId` is 0.
        * If only VPC is supported, the default VPC information is returned.

        You can also use the `Force` parameter to forcibly return a default VPC.

        :param request: Request instance for CreateDefaultVpc.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CreateDefaultVpcRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CreateDefaultVpcResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDefaultVpc", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDefaultVpcResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDirectConnectGateway(self, request):
        """This API is used to create a direct connect gateway.

        :param request: Request instance for CreateDirectConnectGateway.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CreateDirectConnectGatewayRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CreateDirectConnectGatewayResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDirectConnectGateway", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDirectConnectGatewayResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDirectConnectGatewayCcnRoutes(self, request):
        """This API (CreateDirectConnectGatewayCcnRoutes) is used to create the CCN route (IDC IP range) of a Direct Connect gateway.

        :param request: Request instance for CreateDirectConnectGatewayCcnRoutes.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CreateDirectConnectGatewayCcnRoutesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CreateDirectConnectGatewayCcnRoutesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDirectConnectGatewayCcnRoutes", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDirectConnectGatewayCcnRoutesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateFlowLog(self, request):
        """This API is used to create a flow log.

        :param request: Request instance for CreateFlowLog.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CreateFlowLogRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CreateFlowLogResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateFlowLog", params, headers=headers)
            response = json.loads(body)
            model = models.CreateFlowLogResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateHaVip(self, request):
        """This API is used to create a highly available virtual IP (HAVIP).

        :param request: Request instance for CreateHaVip.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CreateHaVipRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CreateHaVipResponse`

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


    def CreateLocalGateway(self, request):
        """This API is used to create a local gateway for a CDC instance.

        :param request: Request instance for CreateLocalGateway.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CreateLocalGatewayRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CreateLocalGatewayResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateLocalGateway", params, headers=headers)
            response = json.loads(body)
            model = models.CreateLocalGatewayResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateNatGateway(self, request):
        """This API is used to create a NAT Gateway.
        Before taking actions on a NAT gateway, ensure that it has been successfully created, namely, the `State` field in the response of the `DescribeNatGateway` API is `AVAILABLE`.

        :param request: Request instance for CreateNatGateway.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CreateNatGatewayRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CreateNatGatewayResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateNatGateway", params, headers=headers)
            response = json.loads(body)
            model = models.CreateNatGatewayResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateNatGatewayDestinationIpPortTranslationNatRule(self, request):
        """This API is used to create the port forwarding rules of a NAT gateway.

        :param request: Request instance for CreateNatGatewayDestinationIpPortTranslationNatRule.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CreateNatGatewayDestinationIpPortTranslationNatRuleRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CreateNatGatewayDestinationIpPortTranslationNatRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateNatGatewayDestinationIpPortTranslationNatRule", params, headers=headers)
            response = json.loads(body)
            model = models.CreateNatGatewayDestinationIpPortTranslationNatRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateNatGatewaySourceIpTranslationNatRule(self, request):
        """This API is used to create SNAT rules for a NAT gateway.

        :param request: Request instance for CreateNatGatewaySourceIpTranslationNatRule.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CreateNatGatewaySourceIpTranslationNatRuleRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CreateNatGatewaySourceIpTranslationNatRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateNatGatewaySourceIpTranslationNatRule", params, headers=headers)
            response = json.loads(body)
            model = models.CreateNatGatewaySourceIpTranslationNatRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateNetDetect(self, request):
        """This API is used to create a network probe.

        :param request: Request instance for CreateNetDetect.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CreateNetDetectRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CreateNetDetectResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateNetDetect", params, headers=headers)
            response = json.loads(body)
            model = models.CreateNetDetectResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateNetworkAcl(self, request):
        """This API is used to create a <a href="https://intl.cloud.tencent.com/document/product/215/20088?from_cn_redirect=1">network ACL</a>.
        * The inbound and outbound rules for a new network ACL are "Deny All" by default. You need to call `ModifyNetworkAclEntries` to set rules for the new network ACL as needed.

        :param request: Request instance for CreateNetworkAcl.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CreateNetworkAclRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CreateNetworkAclResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateNetworkAcl", params, headers=headers)
            response = json.loads(body)
            model = models.CreateNetworkAclResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateNetworkAclQuintupleEntries(self, request):
        """This API is used to add one or more in/outbound rules of the network ACL quintuple.

        :param request: Request instance for CreateNetworkAclQuintupleEntries.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CreateNetworkAclQuintupleEntriesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CreateNetworkAclQuintupleEntriesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateNetworkAclQuintupleEntries", params, headers=headers)
            response = json.loads(body)
            model = models.CreateNetworkAclQuintupleEntriesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateNetworkInterface(self, request):
        """This API is used to create an ENI.
        * You can specify private IP addresses and a primary IP when creating an ENI. The specified private IP must be in the same subnet as the ENI and is not occupied.
        * When creating an ENI, you can specify the number of private IP addresses that you want to apply for. The system will randomly generate private IP addresses.
        * An ENI can only be bound with a limited number of IP addresses. For more information about resource limits, see <a href="/document/product/576/18527">ENI Use Limits</a>.
        * You can bind an existing security group when creating an ENI.
        * You can bind a tag when creating an ENI. The tag list in the response indicates the tags that have been successfully added.
        >?This API is async. You can call the [`DescribeVpcTaskResult`](https://intl.cloud.tencent.com/document/api/215/59037?from_cn_redirect=1) API to query the task result. When the task is completed, you can continue other tasks.
        >

        :param request: Request instance for CreateNetworkInterface.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CreateNetworkInterfaceRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CreateNetworkInterfaceResponse`

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


    def CreateReserveIpAddresses(self, request):
        """This API is used to create a reserved private IP address.

        :param request: Request instance for CreateReserveIpAddresses.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CreateReserveIpAddressesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CreateReserveIpAddressesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateReserveIpAddresses", params, headers=headers)
            response = json.loads(body)
            model = models.CreateReserveIpAddressesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateRouteTable(self, request):
        """This API is used to create a route table.
        * After the VPC instance has been created, the system creates a default route table with which all newly created subnets will be associated. By default, you can use this route table to manage your routing policies. If you have multiple routing policies, you can call the API for creating route tables to create more route tables to manage these routing policies.
        * You can bind a tag when creating a route table. The tag list in the response indicates the tags that have been successfully added.

        :param request: Request instance for CreateRouteTable.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CreateRouteTableRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CreateRouteTableResponse`

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
        """This API is used to create routes.
        * You can batch add routes to a specified route table.

        :param request: Request instance for CreateRoutes.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CreateRoutesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CreateRoutesResponse`

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
        """This API is used to create a security group (SecurityGroup).
        * Note the <a href="https://intl.cloud.tencent.com/document/product/213/12453?from_cn_redirect=1">maximum number of security groups</a> per project in each region under each account.
        * Both the inbound and outbound rules for a newly created security group are "Deny All" by default. You need to call CreateSecurityGroupPolicies to set security group rules based on your needs.
        * You can bind a tag when creating a security group. The tag list in the response indicates the tags that have been successfully added.

        :param request: Request instance for CreateSecurityGroup.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CreateSecurityGroupRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CreateSecurityGroupResponse`

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
        """This API is used to create security group policies (`SecurityGroupPolicy`).

        For parameters of `SecurityGroupPolicySet`,
        <ul>
        <li>`Version`: The version number of a security group policy, which automatically increases by one each time you update the security policy, to prevent expiration of the updated routing policies. If it is left empty, any conflicts will be ignored.</li>
        <li>When creating the `Egress` and `Ingress` polices,<ul>
        <li>`Protocol`: Allows `TCP`, `UDP`, `ICMP`, `ICMPV6`, `GRE` and `ALL`.</li>
        <li>`CidrBlock`: For the classic network, the `CidrBlock` can contain private IPs of Tencent Cloud resources that are not under your account. It does not mean that you can access these devices. The network isolation policies between tenants take priority over the private network policies in security groups.</li>
        <li>`Ipv6CidrBlock`: For the classic network, `Ipv6CidrBlock` can contain private IPv6 addresses of Tencent Cloud resources that are not under your account. It does not mean that you can access these devices. The network isolation policies between tenants take priority over the private network policies in security groups.</li>
        <li>`SecurityGroupId`: ID of the security group to create policies. </li>
        <li>`Port`: A single port (“80”) or a port range ("8000-8010"). This parameter is only available when `Protocol` is `TCP` or `UDP`.</li>
        <li>`Action`: `ACCEPT` or `DROP`.</li>
        <li><code>CidrBlock</code>, <code>Ipv6CidrBlock</code>, <code>SecurityGroupId</code>, and <code>AddressTemplate</code> are mutually exclusive. <code>Protocol</code> + <code>Port</code> and <code>ServiceTemplate</code> are mutually exclusive. <code>IPv6CidrBlock</code> and <code>ICMP</code> are mutually exclusive; to use them, enter <code>ICMPV6</code>.</li>
        <li>You can only create policies in one direction in each request. To specify the `PolicyIndex` parameter, use the same index number in policies. If you want to insert a rule before the first rule, enter 0; if you want to add a rule after the last rule, leave it empty.</li>
        </ul></li></ul>

        :param request: Request instance for CreateSecurityGroupPolicies.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CreateSecurityGroupPoliciesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CreateSecurityGroupPoliciesResponse`

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


    def CreateSecurityGroupWithPolicies(self, request):
        """This API is used to create a security group, and add security group policies.
        * For the the upper limit of security groups per project in each region under each account, <a href="https://intl.cloud.tencent.com/document/product/213/12453?from_cn_redirect=1">see here</a>
        * For newly created security groups, the inbound and outbound policies are set to `Deny All` by default. You need to call <a href="https://intl.cloud.tencent.com/document/product/215/15807?from_cn_redirect=1">CreateSecurityGroupPolicies</a>
        to change it.

        Description:
        * `Version`: The version number of a security group policy. It automatically increments by 1 every time you update the security policy, so to prevent the expiration of the updated policies. If this field is left empty, any conflicts will be ignored.
        * `Protocol`: Values can be `TCP`, `UDP`, `ICMP`, `ICMPV6`, `GRE`, and `ALL`.
        * `CidrBlock`: Enter a CIDR block in the correct format. In the classic network, even if the CIDR block specified in `CidrBlock` contains the Tencent Cloud private IPs not used for CVMs under your Tencent Cloud account, it does not mean this policy allows you to access those resources. The network isolation policies between tenants take priority over the private network policies in security groups.
        * `Ipv6CidrBlock`: Enter an IPv6 CIDR block in the correct format. In the classic network, even if the CIDR block specified in `Ipv6CidrBlock` contains the Tencent Cloud private IPv6 addresses not used for CVMs under your Tencent Cloud account, it does not mean this policy allows you to access those resources. The network isolation policies between tenants take priority over the private network policies in security groups.
        * `SecurityGroupId`: ID of the security group. It can be the ID of a security group to be modified, or the ID of another security group in the same project. All private IPs of all CVMs under the security group will be covered. If this field is used, the policy will automatically change according to the CVM associated with the group ID while being used to match network messages. You don't need to change it manually.
        * `Port`: Enter a single port number (such as `80`), or a port range (such as `8000-8010`). `Port` is only applicable when `Protocol` is `TCP` or `UDP`. If `Protocol` is not `TCP` or `UDP`, `Protocol` and `Port` cannot be both specified.
        * `Action`: Values can be `ACCEPT` or `DROP`.
        * `CidrBlock`, `Ipv6CidrBlock`, `SecurityGroupId`, and `AddressTemplate` are exclusive to one another. "Protocol + Port" and `ServiceTemplate` are mutually exclusive.
        * Only policies in one direction can be created in each request. If you need to specify the `PolicyIndex` parameter, the indexes of policies must be consistent.

        :param request: Request instance for CreateSecurityGroupWithPolicies.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CreateSecurityGroupWithPoliciesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CreateSecurityGroupWithPoliciesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateSecurityGroupWithPolicies", params, headers=headers)
            response = json.loads(body)
            model = models.CreateSecurityGroupWithPoliciesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateServiceTemplate(self, request):
        """This API (CreateServiceTemplate) is used to create a protocol port template.

        :param request: Request instance for CreateServiceTemplate.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CreateServiceTemplateRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CreateServiceTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateServiceTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.CreateServiceTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateServiceTemplateGroup(self, request):
        """This API (CreateServiceTemplateGroup) is used to create a protocol port template group.

        :param request: Request instance for CreateServiceTemplateGroup.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CreateServiceTemplateGroupRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CreateServiceTemplateGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateServiceTemplateGroup", params, headers=headers)
            response = json.loads(body)
            model = models.CreateServiceTemplateGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateSnapshotPolicies(self, request):
        """This API is used to create snapshot policies.

        :param request: Request instance for CreateSnapshotPolicies.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CreateSnapshotPoliciesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CreateSnapshotPoliciesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateSnapshotPolicies", params, headers=headers)
            response = json.loads(body)
            model = models.CreateSnapshotPoliciesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateSubnet(self, request):
        """This API is used to create a subnet.
        * You must create a VPC instance before creating a subnet.
        * After the subnet is successfully created, its IP address range cannot be modified. The subnet IP address range must fall within the VPC IP address range. They can be the same if the VPC instance has only one subnet. We recommend that you keep the subnet IP address range within the VPC IP address range to reserve IP address ranges for other subnets.
        * The subnet mask of the smallest IP address range that can be created is 28 (16 IP addresses), and that of the largest IP address range is 16 (65,536 IP addresses).
        * IP address ranges of different subnets cannot overlap with each other within the same VPC instance.
        * A subnet is automatically associated with the default route table once created.
        * You can bind a tag when creating a subnet. The tag list in the response indicates the tags that have been successfully added.

        :param request: Request instance for CreateSubnet.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CreateSubnetRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CreateSubnetResponse`

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


    def CreateSubnets(self, request):
        """This API is used to create subnets in batches.
        * You must create a VPC instance before creating a subnet.
        * After the subnet is successfully created, its IP address range cannot be modified. The subnet IP address range must fall within the VPC IP address range. They can be the same if the VPC has only one subnet. We recommend that you keep the subnet IP address range within the VPC IP address range to reserve IP address ranges for other subnets.
        * The subnet mask of the smallest IP address range that can be created is 28 (16 IP addresses), and that of the largest IP address range is 16 (65,536 IP addresses).
        * IP address ranges of different subnets cannot overlap with each other within the same VPC instance.
        * A subnet is automatically associated with the default route table once created.
        * You can bind a tag when creating a subnet. The tag list in the response indicates the tags that have been successfully added.

        :param request: Request instance for CreateSubnets.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CreateSubnetsRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CreateSubnetsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateSubnets", params, headers=headers)
            response = json.loads(body)
            model = models.CreateSubnetsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateVpc(self, request):
        """This API is used to create a VPC instance.
        * The subnet mask of the smallest IP address range that can be created is 28 (16 IP addresses), that of the largest IP address ranges 10.0.0.0/12 and 172.16.0.0/12 is 12 (1,048,576 IP addresses), and that of the largest IP address range 192.168.0.0/16 is 16 (65,536 IP addresses). For more information on how to plan VPC IP ranges, see [Network Planning](https://intl.cloud.tencent.com/document/product/215/30313?from_cn_redirect=1).
        * The number of VPC instances that can be created in a region is limited. For more information, see <a href="https://intl.cloud.tencent.com/doc/product/215/537?from_cn_redirect=1" title="VPC Use Limits">VPC Use Limits</a>. To request more resources, [submit a ticket](https://console.cloud.tencent.com/workorder/category).
        * You can bind tags when creating a VPC instance. The tag list in the response indicates the tags that have been successfully added.

        :param request: Request instance for CreateVpc.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CreateVpcRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CreateVpcResponse`

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


    def CreateVpcEndPoint(self, request):
        """This API is used to create an endpoint.

        :param request: Request instance for CreateVpcEndPoint.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CreateVpcEndPointRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CreateVpcEndPointResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateVpcEndPoint", params, headers=headers)
            response = json.loads(body)
            model = models.CreateVpcEndPointResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateVpcEndPointService(self, request):
        """This API is used to create an endpoint service.

        :param request: Request instance for CreateVpcEndPointService.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CreateVpcEndPointServiceRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CreateVpcEndPointServiceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateVpcEndPointService", params, headers=headers)
            response = json.loads(body)
            model = models.CreateVpcEndPointServiceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateVpcEndPointServiceWhiteList(self, request):
        """This API is used to create the endpoint service allowlist.

        :param request: Request instance for CreateVpcEndPointServiceWhiteList.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CreateVpcEndPointServiceWhiteListRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CreateVpcEndPointServiceWhiteListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateVpcEndPointServiceWhiteList", params, headers=headers)
            response = json.loads(body)
            model = models.CreateVpcEndPointServiceWhiteListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateVpnConnection(self, request):
        """This API is used to create a VPN tunnel.
        >?This API is async. You can call the [`DescribeVpcTaskResult`](https://intl.cloud.tencent.com/document/api/215/59037?from_cn_redirect=1) API to query the task result. When the task is completed, you can continue other tasks.
        >

        :param request: Request instance for CreateVpnConnection.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CreateVpnConnectionRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CreateVpnConnectionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateVpnConnection", params, headers=headers)
            response = json.loads(body)
            model = models.CreateVpnConnectionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateVpnGateway(self, request):
        """This API (CreateVpnGateway) is used to create a VPN gateway.

        :param request: Request instance for CreateVpnGateway.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CreateVpnGatewayRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CreateVpnGatewayResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateVpnGateway", params, headers=headers)
            response = json.loads(body)
            model = models.CreateVpnGatewayResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateVpnGatewayRoutes(self, request):
        """This API is used to create destination routes of a route-based VPN gateway.

        :param request: Request instance for CreateVpnGatewayRoutes.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CreateVpnGatewayRoutesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CreateVpnGatewayRoutesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateVpnGatewayRoutes", params, headers=headers)
            response = json.loads(body)
            model = models.CreateVpnGatewayRoutesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteAddressTemplate(self, request):
        """This API (DeleteAddressTemplate) is used to delete an IP address template.

        :param request: Request instance for DeleteAddressTemplate.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DeleteAddressTemplateRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DeleteAddressTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteAddressTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteAddressTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteAddressTemplateGroup(self, request):
        """This API (DeleteAddressTemplateGroup) is used to delete an IP address template group.

        :param request: Request instance for DeleteAddressTemplateGroup.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DeleteAddressTemplateGroupRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DeleteAddressTemplateGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteAddressTemplateGroup", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteAddressTemplateGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteAssistantCidr(self, request):
        """This API is used to delete a secondary CIDR block.

        :param request: Request instance for DeleteAssistantCidr.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DeleteAssistantCidrRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DeleteAssistantCidrResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteAssistantCidr", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteAssistantCidrResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteBandwidthPackage(self, request):
        """This API is used to delete bandwidth packages, including [device bandwidth packages](https://intl.cloud.tencent.com/document/product/684/15246?from_cn_redirect=1#.E8.AE.BE.E5.A4.87.E5.B8.A6.E5.AE.BD.E5.8C.85) and [IP bandwidth packages](https://intl.cloud.tencent.com/document/product/684/15246?from_cn_redirect=1#ip-.E5.B8.A6.E5.AE.BD.E5.8C.85).

        :param request: Request instance for DeleteBandwidthPackage.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DeleteBandwidthPackageRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DeleteBandwidthPackageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteBandwidthPackage", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteBandwidthPackageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteCcn(self, request):
        """This API (DeleteCcn) is used to delete CCNs.
        * After deletion, the routes between all instances associated with the CCN will be deleted, and the network will be interrupted. Please confirm this operation in advance.
        * CCN deletion is an irreversible operation. Please proceed with caution.

        :param request: Request instance for DeleteCcn.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DeleteCcnRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DeleteCcnResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteCcn", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteCcnResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteCustomerGateway(self, request):
        """This API (DeleteCustomerGateway) is used to delete customer gateways.

        :param request: Request instance for DeleteCustomerGateway.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DeleteCustomerGatewayRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DeleteCustomerGatewayResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteCustomerGateway", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteCustomerGatewayResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteDirectConnectGateway(self, request):
        """This API is used to delete a direct connect gateway.
        <li>For a NAT gateway, NAT and ACL rules will be cleared upon the deletion of a direct connect gateway.
        <li>After the deletion of a direct connect gateway, the routing policy associated with the gateway in the route table will also be deleted.
        This API is completed asynchronously. If you need to query the async job execution results, please use the `RequestId` returned by this API to poll the `QueryTask` API.

        :param request: Request instance for DeleteDirectConnectGateway.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DeleteDirectConnectGatewayRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DeleteDirectConnectGatewayResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteDirectConnectGateway", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteDirectConnectGatewayResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteDirectConnectGatewayCcnRoutes(self, request):
        """This API (DeleteDirectConnectGatewayCcnRoutes) is used to delete the CCN routes (IDC IP range) of a Direct Connect gateway.

        :param request: Request instance for DeleteDirectConnectGatewayCcnRoutes.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DeleteDirectConnectGatewayCcnRoutesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DeleteDirectConnectGatewayCcnRoutesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteDirectConnectGatewayCcnRoutes", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteDirectConnectGatewayCcnRoutesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteFlowLog(self, request):
        """This API is used to delete a flow log.

        :param request: Request instance for DeleteFlowLog.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DeleteFlowLogRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DeleteFlowLogResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteFlowLog", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteFlowLogResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteHaVip(self, request):
        """This API is used to delete an HAVIP. <br />
        This API is completed asynchronously. If you need to query the execution result of an async task, please use the `RequestId` returned by this API to poll the `DescribeVpcTaskResult` API.

        :param request: Request instance for DeleteHaVip.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DeleteHaVipRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DeleteHaVipResponse`

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


    def DeleteLocalGateway(self, request):
        """This API is used to delete the local gateway of a CDC instance.

        :param request: Request instance for DeleteLocalGateway.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DeleteLocalGatewayRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DeleteLocalGatewayResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteLocalGateway", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteLocalGatewayResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteNatGateway(self, request):
        """This API is used to delete a NAT gateway.
        When a NAT gateway is deleted, all routes containing this gateway are deleted automatically, and the elastic IP is unbound.

        :param request: Request instance for DeleteNatGateway.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DeleteNatGatewayRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DeleteNatGatewayResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteNatGateway", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteNatGatewayResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteNatGatewayDestinationIpPortTranslationNatRule(self, request):
        """This API is used to delete the port forwarding rule of a NAT gateway.

        :param request: Request instance for DeleteNatGatewayDestinationIpPortTranslationNatRule.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DeleteNatGatewayDestinationIpPortTranslationNatRuleRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DeleteNatGatewayDestinationIpPortTranslationNatRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteNatGatewayDestinationIpPortTranslationNatRule", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteNatGatewayDestinationIpPortTranslationNatRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteNatGatewaySourceIpTranslationNatRule(self, request):
        """This API is used to delete a SNAT forwarding rule of a NAT gateway.

        :param request: Request instance for DeleteNatGatewaySourceIpTranslationNatRule.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DeleteNatGatewaySourceIpTranslationNatRuleRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DeleteNatGatewaySourceIpTranslationNatRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteNatGatewaySourceIpTranslationNatRule", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteNatGatewaySourceIpTranslationNatRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteNetDetect(self, request):
        """This API is used to delete a network probe.

        :param request: Request instance for DeleteNetDetect.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DeleteNetDetectRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DeleteNetDetectResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteNetDetect", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteNetDetectResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteNetworkAcl(self, request):
        """This API is used to delete a network ACL.

        :param request: Request instance for DeleteNetworkAcl.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DeleteNetworkAclRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DeleteNetworkAclResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteNetworkAcl", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteNetworkAclResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteNetworkAclQuintupleEntries(self, request):
        """This API is used to delete specified in/outbound rules of the network ACL quintuple. In the `NetworkAclQuintupleEntrySet` parameters, `NetworkAclQuintupleEntryId` is required for `NetworkAclQuintupleEntry`.

        :param request: Request instance for DeleteNetworkAclQuintupleEntries.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DeleteNetworkAclQuintupleEntriesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DeleteNetworkAclQuintupleEntriesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteNetworkAclQuintupleEntries", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteNetworkAclQuintupleEntriesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteNetworkInterface(self, request):
        """This API is used to delete an ENI.
        * An ENI cannot be deleted when it’s bound to a CVM.
         * After the deletion, all of its private IP addresses will be released.

        This API is completed asynchronously. If you need to query the execution result of an async task, please use the `RequestId` returned by this API to poll the `DescribeVpcTaskResult` API.

        :param request: Request instance for DeleteNetworkInterface.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DeleteNetworkInterfaceRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DeleteNetworkInterfaceResponse`

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


    def DeleteReserveIpAddresses(self, request):
        """This API is used to delete a reserved private IP address.

        :param request: Request instance for DeleteReserveIpAddresses.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DeleteReserveIpAddressesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DeleteReserveIpAddressesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteReserveIpAddresses", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteReserveIpAddressesResponse()
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
        :type request: :class:`tencentcloud.vpc.v20170312.models.DeleteRouteTableRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DeleteRouteTableResponse`

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
        """This API (DeleteRoutes) is used to delete routing policies in batches from a route table.

        :param request: Request instance for DeleteRoutes.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DeleteRoutesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DeleteRoutesResponse`

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
        """This API (DeleteSecurityGroup) is used to delete security groups (SecurityGroup).
        * Only security groups under the current account can be deleted.
        * A security group cannot be deleted directly if its instance ID is used in the policy of another security group. You need to modify the policy first and then delete the security group.
        * A security group cannot be recovered after deletion, please proceed with caution.

        :param request: Request instance for DeleteSecurityGroup.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DeleteSecurityGroupRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DeleteSecurityGroupResponse`

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
        """This API (DeleteSecurityGroupPolicies) is used to delete security group policies (SecurityGroupPolicy).
        * SecurityGroupPolicySet.Version is used to specify the version of the security group you are operating. If the specified Version number differs from the latest version of the current security group, a failure will be returned. If Version is not specified, the policy of the specified PolicyIndex will be deleted directly.

        :param request: Request instance for DeleteSecurityGroupPolicies.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DeleteSecurityGroupPoliciesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DeleteSecurityGroupPoliciesResponse`

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


    def DeleteServiceTemplate(self, request):
        """This API (DeleteServiceTemplate) is used to delete a protocol port template.

        :param request: Request instance for DeleteServiceTemplate.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DeleteServiceTemplateRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DeleteServiceTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteServiceTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteServiceTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteServiceTemplateGroup(self, request):
        """This API (DeleteServiceTemplateGroup) is used to delete a protocol port template group.

        :param request: Request instance for DeleteServiceTemplateGroup.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DeleteServiceTemplateGroupRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DeleteServiceTemplateGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteServiceTemplateGroup", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteServiceTemplateGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteSnapshotPolicies(self, request):
        """This API is used to delete snapshot policies.

        :param request: Request instance for DeleteSnapshotPolicies.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DeleteSnapshotPoliciesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DeleteSnapshotPoliciesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteSnapshotPolicies", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteSnapshotPoliciesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteSubnet(self, request):
        """This API is used to delete a subnet.
        * Remove all resources in the subnet before deleting it

        :param request: Request instance for DeleteSubnet.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DeleteSubnetRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DeleteSubnetResponse`

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


    def DeleteTemplateMember(self, request):
        """This API is used to delete a parameter template of the IP address, protocol port, IP address group, or protocol port group type.

        :param request: Request instance for DeleteTemplateMember.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DeleteTemplateMemberRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DeleteTemplateMemberResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteTemplateMember", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteTemplateMemberResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteTrafficPackages(self, request):
        """This API is used to delete traffic packages. Note that only non-valid traffic packages can be deleted.

        :param request: Request instance for DeleteTrafficPackages.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DeleteTrafficPackagesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DeleteTrafficPackagesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteTrafficPackages", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteTrafficPackagesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteVpc(self, request):
        """This API (DeleteVpc) is used to delete VPCs.
        * Before deleting a VPC, ensure that the VPC contains no resources, including CVMs, cloud databases, NoSQL databases, VPN gateways, direct connect gateways, load balancers, peering connections, and basic network devices that are linked to the VPC.
        * The deletion of VPCs is irreversible. Proceed with caution.

        :param request: Request instance for DeleteVpc.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DeleteVpcRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DeleteVpcResponse`

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


    def DeleteVpcEndPoint(self, request):
        """This API is used to delete an endpoint.

        :param request: Request instance for DeleteVpcEndPoint.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DeleteVpcEndPointRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DeleteVpcEndPointResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteVpcEndPoint", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteVpcEndPointResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteVpcEndPointService(self, request):
        """This API is used to delete an endpoint service.


        :param request: Request instance for DeleteVpcEndPointService.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DeleteVpcEndPointServiceRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DeleteVpcEndPointServiceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteVpcEndPointService", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteVpcEndPointServiceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteVpcEndPointServiceWhiteList(self, request):
        """This API is used to delete the endpoint service allowlist.

        :param request: Request instance for DeleteVpcEndPointServiceWhiteList.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DeleteVpcEndPointServiceWhiteListRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DeleteVpcEndPointServiceWhiteListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteVpcEndPointServiceWhiteList", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteVpcEndPointServiceWhiteListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteVpnConnection(self, request):
        """This API is used to delete a VPN tunnel.

        :param request: Request instance for DeleteVpnConnection.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DeleteVpnConnectionRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DeleteVpnConnectionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteVpnConnection", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteVpnConnectionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteVpnGateway(self, request):
        """This API (DeleteVpnGateway) is used to delete a VPN gateway. Currently, only deletion of pay-as-you-go IPSEC gateway instances in running status is supported.

        :param request: Request instance for DeleteVpnGateway.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DeleteVpnGatewayRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DeleteVpnGatewayResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteVpnGateway", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteVpnGatewayResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteVpnGatewayRoutes(self, request):
        """This API is used to delete routes of a VPN gateway.

        :param request: Request instance for DeleteVpnGatewayRoutes.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DeleteVpnGatewayRoutesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DeleteVpnGatewayRoutesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteVpnGatewayRoutes", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteVpnGatewayRoutesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAccountAttributes(self, request):
        """This API (DescribeAccountAttributes) is used to query your account attributes.

        :param request: Request instance for DescribeAccountAttributes.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeAccountAttributesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeAccountAttributesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAccountAttributes", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAccountAttributesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAddressQuota(self, request):
        """This API (DescribeAddressQuota) is used to query the quota information of your [Elastic IP](https://intl.cloud.tencent.com/document/product/213/1941?from_cn_redirect=1) (EIP) in the current region. For more information, see [EIP product introduction](https://intl.cloud.tencent.com/document/product/213/5733?from_cn_redirect=1).

        :param request: Request instance for DescribeAddressQuota.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeAddressQuotaRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeAddressQuotaResponse`

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


    def DescribeAddressTemplateGroups(self, request):
        """This API (DescribeAddressTemplateGroups) is used to query an IP address template group.

        :param request: Request instance for DescribeAddressTemplateGroups.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeAddressTemplateGroupsRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeAddressTemplateGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAddressTemplateGroups", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAddressTemplateGroupsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAddressTemplates(self, request):
        """This API (DescribeAddressTemplates) is used to query an IP address template.

        :param request: Request instance for DescribeAddressTemplates.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeAddressTemplatesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeAddressTemplatesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAddressTemplates", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAddressTemplatesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAddresses(self, request):
        """This API (DescribeAddresses) is used to query the information of one or multiple [Elastic IPs](https://intl.cloud.tencent.com/document/product/213/1941?from_cn_redirect=1).
        * If the parameter is empty, a number (as specified by the `Limit`, the default value is 20) of EIPs will be returned.

        :param request: Request instance for DescribeAddresses.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeAddressesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeAddressesResponse`

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


    def DescribeAssistantCidr(self, request):
        """This API is used to query the list of secondary CIDR blocks.

        :param request: Request instance for DescribeAssistantCidr.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeAssistantCidrRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeAssistantCidrResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssistantCidr", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssistantCidrResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBandwidthPackageBillUsage(self, request):
        """This API is used to query the current billable usage of a pay-as-you-go bandwidth package.

        :param request: Request instance for DescribeBandwidthPackageBillUsage.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeBandwidthPackageBillUsageRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeBandwidthPackageBillUsageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBandwidthPackageBillUsage", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBandwidthPackageBillUsageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBandwidthPackageQuota(self, request):
        """This API is used to query the maximum and used number of bandwidth packages under the account in the current region.

        :param request: Request instance for DescribeBandwidthPackageQuota.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeBandwidthPackageQuotaRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeBandwidthPackageQuotaResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBandwidthPackageQuota", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBandwidthPackageQuotaResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBandwidthPackageResources(self, request):
        """This API is used to query resources in a bandwidth package based on the unique package ID. You can filter the result by specifying conditions and paginate the query results.

        :param request: Request instance for DescribeBandwidthPackageResources.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeBandwidthPackageResourcesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeBandwidthPackageResourcesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBandwidthPackageResources", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBandwidthPackageResourcesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBandwidthPackages(self, request):
        """This API is used to query bandwidth package information, including the unique ID of the bandwidth package, the type, the billing mode, the name, and the resource information.

        :param request: Request instance for DescribeBandwidthPackages.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeBandwidthPackagesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeBandwidthPackagesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBandwidthPackages", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBandwidthPackagesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCcnAttachedInstances(self, request):
        """This API (DescribeCcnAttachedInstances) is used to query the network instances associated with the CCN instance.

        :param request: Request instance for DescribeCcnAttachedInstances.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeCcnAttachedInstancesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeCcnAttachedInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCcnAttachedInstances", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCcnAttachedInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCcnRegionBandwidthLimits(self, request):
        """This API is used to query the outbound bandwidth caps of all regions connected with a CCN instance. The API only returns regions included in the associated network instances.

        :param request: Request instance for DescribeCcnRegionBandwidthLimits.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeCcnRegionBandwidthLimitsRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeCcnRegionBandwidthLimitsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCcnRegionBandwidthLimits", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCcnRegionBandwidthLimitsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCcnRoutes(self, request):
        """This API (DescribeCcnRoutes) is used to query routes that have been added to a CCN.

        :param request: Request instance for DescribeCcnRoutes.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeCcnRoutesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeCcnRoutesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCcnRoutes", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCcnRoutesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCcns(self, request):
        """This API (DescribeCcns) is used to query the CCN list.

        :param request: Request instance for DescribeCcns.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeCcnsRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeCcnsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCcns", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCcnsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeClassicLinkInstances(self, request):
        """This API (DescribeClassicLinkInstances) is used to query the Classiclink instances list.

        :param request: Request instance for DescribeClassicLinkInstances.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeClassicLinkInstancesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeClassicLinkInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClassicLinkInstances", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeClassicLinkInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCrossBorderCompliance(self, request):
        """This API is used to query the compliance review requests created by the user.
        A service provider can query all review requests created by any `APPID` under its account. Other users can only query their own review requests.

        :param request: Request instance for DescribeCrossBorderCompliance.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeCrossBorderComplianceRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeCrossBorderComplianceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCrossBorderCompliance", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCrossBorderComplianceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCustomerGatewayVendors(self, request):
        """This API (DescribeCustomerGatewayVendors) is used to query the information of supported customer gateway vendors.

        :param request: Request instance for DescribeCustomerGatewayVendors.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeCustomerGatewayVendorsRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeCustomerGatewayVendorsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCustomerGatewayVendors", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCustomerGatewayVendorsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCustomerGateways(self, request):
        """This API (DescribeCustomerGateways) is used to query the customer gateway list.

        :param request: Request instance for DescribeCustomerGateways.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeCustomerGatewaysRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeCustomerGatewaysResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCustomerGateways", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCustomerGatewaysResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDirectConnectGatewayCcnRoutes(self, request):
        """This API (DescribeDirectConnectGatewayCcnRoutes) is used to query the CCN routes (IDC IP range) of the Direct Connect gateway.

        :param request: Request instance for DescribeDirectConnectGatewayCcnRoutes.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeDirectConnectGatewayCcnRoutesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeDirectConnectGatewayCcnRoutesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDirectConnectGatewayCcnRoutes", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDirectConnectGatewayCcnRoutesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDirectConnectGateways(self, request):
        """This API is used to query direct connect gateways.

        :param request: Request instance for DescribeDirectConnectGateways.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeDirectConnectGatewaysRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeDirectConnectGatewaysResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDirectConnectGateways", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDirectConnectGatewaysResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeFlowLog(self, request):
        """This API is used to query the information of a flow log.

        :param request: Request instance for DescribeFlowLog.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeFlowLogRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeFlowLogResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeFlowLog", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeFlowLogResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeFlowLogs(self, request):
        """This API is used to query all the flow logs of the current account.

        :param request: Request instance for DescribeFlowLogs.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeFlowLogsRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeFlowLogsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeFlowLogs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeFlowLogsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeGatewayFlowMonitorDetail(self, request):
        """This API is used to query the traffic monitoring details of the gateway.
        * You can only use this API to query a single gateway instance, which means you must pass in only one of `VpnId`, `DirectConnectGatewayId`, `PeeringConnectionId`, or `NatId`.
        * If the gateway has traffic, but no data is returned when this API is called, please check whether gateway traffic monitoring has been enabled in the corresponding gateway details page in the console.

        :param request: Request instance for DescribeGatewayFlowMonitorDetail.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeGatewayFlowMonitorDetailRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeGatewayFlowMonitorDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeGatewayFlowMonitorDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeGatewayFlowMonitorDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeGatewayFlowQos(self, request):
        """This API is used to query the inbound IP bandwidth limit of a gateway.

        :param request: Request instance for DescribeGatewayFlowQos.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeGatewayFlowQosRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeGatewayFlowQosResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeGatewayFlowQos", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeGatewayFlowQosResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeHaVips(self, request):
        """This API (DescribeHaVips) is used to query the list of highly available virtual IPs (HAVIP).

        :param request: Request instance for DescribeHaVips.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeHaVipsRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeHaVipsResponse`

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


    def DescribeIPv6Addresses(self, request):
        """This API is used to query detailed information of one or more EIPv6 instances.

        - You can query EIPv6 and traditional EIPv6 instance information in a specified region.
        - The system returns a certain number (as specified by the Limit, the default value is 20) of EIPv6 instances of the current user if the parameter is empty.

        :param request: Request instance for DescribeIPv6Addresses.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeIPv6AddressesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeIPv6AddressesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeIPv6Addresses", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeIPv6AddressesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstanceJumbo(self, request):
        """This API is used to check whether Cloud Virtual Machines support jumbo frames.
        Usage limits.
        This API is used to perform operations that require CAM policy authorization and read access to the corresponding instance. The API accesses CVM instances, so it verifies whether there are CAM permissions for the instance. For example: CAM action allows vpc:DescribeInstanceJumbo; resource allows qcs::cvm:ap-guangzhou:uin/2126195383:instance/*.
        This API is used to check the jumbo frame status before and after instance migration. The status returned by this API may be inconsistent before and after migration. You need to check whether the host machines of the instance before and after migration both support jumbo frames. One possible reason is that the instance has been migrated to a host machine that does not support jumbo frames.

        :param request: Request instance for DescribeInstanceJumbo.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeInstanceJumboRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeInstanceJumboResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstanceJumbo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstanceJumboResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeIp6Addresses(self, request):
        """This API is used to query the detailed information on one or multiple classic elastic public IPv6 instances.

        :param request: Request instance for DescribeIp6Addresses.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeIp6AddressesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeIp6AddressesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeIp6Addresses", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeIp6AddressesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeIpGeolocationDatabaseUrl(self, request):
        """This API is used to obtain the download link of an IP location database.
        <font color="#FF0000">This API will be discontinued soon and is only available for existing users.</font>

        :param request: Request instance for DescribeIpGeolocationDatabaseUrl.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeIpGeolocationDatabaseUrlRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeIpGeolocationDatabaseUrlResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeIpGeolocationDatabaseUrl", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeIpGeolocationDatabaseUrlResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeIpGeolocationInfos(self, request):
        """This API is used to query the location and network information of one or more IP addresses.
        <font color="#FF0000">This API will be discontinued soon and is only available for existing users.</font>

        :param request: Request instance for DescribeIpGeolocationInfos.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeIpGeolocationInfosRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeIpGeolocationInfosResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeIpGeolocationInfos", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeIpGeolocationInfosResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLocalGateway(self, request):
        """This API is used to query local gateways of a CDC instance.

        :param request: Request instance for DescribeLocalGateway.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeLocalGatewayRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeLocalGatewayResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLocalGateway", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLocalGatewayResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeNatGatewayDestinationIpPortTranslationNatRules(self, request):
        """This API is used to query the array of objects of a NAT gateway's port forwarding rules.

        :param request: Request instance for DescribeNatGatewayDestinationIpPortTranslationNatRules.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeNatGatewayDestinationIpPortTranslationNatRulesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeNatGatewayDestinationIpPortTranslationNatRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeNatGatewayDestinationIpPortTranslationNatRules", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeNatGatewayDestinationIpPortTranslationNatRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeNatGatewayDirectConnectGatewayRoute(self, request):
        """This API is used to query the routes between a NAT gateway and Direct Connect.

        :param request: Request instance for DescribeNatGatewayDirectConnectGatewayRoute.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeNatGatewayDirectConnectGatewayRouteRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeNatGatewayDirectConnectGatewayRouteResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeNatGatewayDirectConnectGatewayRoute", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeNatGatewayDirectConnectGatewayRouteResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeNatGatewaySourceIpTranslationNatRules(self, request):
        """This API is used to query the NAT gateway's SNAT forwarding rules.

        :param request: Request instance for DescribeNatGatewaySourceIpTranslationNatRules.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeNatGatewaySourceIpTranslationNatRulesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeNatGatewaySourceIpTranslationNatRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeNatGatewaySourceIpTranslationNatRules", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeNatGatewaySourceIpTranslationNatRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeNatGateways(self, request):
        """This API is used to query NAT gateways.

        :param request: Request instance for DescribeNatGateways.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeNatGatewaysRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeNatGatewaysResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeNatGateways", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeNatGatewaysResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeNetDetectStates(self, request):
        """This API (DescribeNetDetectStates) is used to query the list of network detection verification results.

        :param request: Request instance for DescribeNetDetectStates.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeNetDetectStatesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeNetDetectStatesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeNetDetectStates", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeNetDetectStatesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeNetDetects(self, request):
        """This API (DescribeNetDetects) is used to query the list of network detection instances.

        :param request: Request instance for DescribeNetDetects.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeNetDetectsRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeNetDetectsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeNetDetects", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeNetDetectsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeNetworkAclQuintupleEntries(self, request):
        """This API is used to query the list of in/outbound network ACL quintuple entries.

        :param request: Request instance for DescribeNetworkAclQuintupleEntries.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeNetworkAclQuintupleEntriesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeNetworkAclQuintupleEntriesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeNetworkAclQuintupleEntries", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeNetworkAclQuintupleEntriesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeNetworkAcls(self, request):
        """This API is used to query a list of network ACLs.

        :param request: Request instance for DescribeNetworkAcls.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeNetworkAclsRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeNetworkAclsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeNetworkAcls", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeNetworkAclsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeNetworkInterfaceLimit(self, request):
        """This API (DescribeNetworkInterfaceLimit) is used to query the ENI quota based on the ID of CVM instance or ENI. It returns the ENI quota to which the CVM instance can be bound and the IP address quota that can be allocated to the ENI.

        :param request: Request instance for DescribeNetworkInterfaceLimit.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeNetworkInterfaceLimitRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeNetworkInterfaceLimitResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeNetworkInterfaceLimit", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeNetworkInterfaceLimitResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeNetworkInterfaces(self, request):
        """This API (DescribeNetworkInterfaces) is used to query the ENI list.

        :param request: Request instance for DescribeNetworkInterfaces.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeNetworkInterfacesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeNetworkInterfacesResponse`

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


    def DescribeReserveIpAddresses(self, request):
        """This API is used to query reserved private IP addresses.

        :param request: Request instance for DescribeReserveIpAddresses.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeReserveIpAddressesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeReserveIpAddressesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeReserveIpAddresses", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeReserveIpAddressesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRouteTables(self, request):
        """This API is used to query route tables.

        :param request: Request instance for DescribeRouteTables.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeRouteTablesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeRouteTablesResponse`

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
        """This API (DescribeSecurityGroupAssociationStatistics) is used to query statistics on the instances associated with a security group.

        :param request: Request instance for DescribeSecurityGroupAssociationStatistics.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeSecurityGroupAssociationStatisticsRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeSecurityGroupAssociationStatisticsResponse`

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


    def DescribeSecurityGroupPolicies(self, request):
        """This API (DescribeSecurityGroupPolicies) is used to query security group policies.

        :param request: Request instance for DescribeSecurityGroupPolicies.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeSecurityGroupPoliciesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeSecurityGroupPoliciesResponse`

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


    def DescribeSecurityGroupReferences(self, request):
        """This API (DescribeSecurityGroupReferences) is used to query referred security groups.

        :param request: Request instance for DescribeSecurityGroupReferences.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeSecurityGroupReferencesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeSecurityGroupReferencesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSecurityGroupReferences", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSecurityGroupReferencesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSecurityGroups(self, request):
        """This API (DescribeSecurityGroups) is used to query security groups.

        :param request: Request instance for DescribeSecurityGroups.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeSecurityGroupsRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeSecurityGroupsResponse`

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


    def DescribeServiceTemplateGroups(self, request):
        """This API (DescribeServiceTemplateGroups) is used to query a protocol port template group.

        :param request: Request instance for DescribeServiceTemplateGroups.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeServiceTemplateGroupsRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeServiceTemplateGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeServiceTemplateGroups", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeServiceTemplateGroupsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeServiceTemplates(self, request):
        """This API (DescribeServiceTemplates) is used to query protocol port templates.

        :param request: Request instance for DescribeServiceTemplates.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeServiceTemplatesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeServiceTemplatesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeServiceTemplates", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeServiceTemplatesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSgSnapshotFileContent(self, request):
        """This API is used to query the snapshot file contents.

        :param request: Request instance for DescribeSgSnapshotFileContent.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeSgSnapshotFileContentRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeSgSnapshotFileContentResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSgSnapshotFileContent", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSgSnapshotFileContentResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSnapshotAttachedInstances(self, request):
        """This API is used to query instances associated with a snapshot policy.

        :param request: Request instance for DescribeSnapshotAttachedInstances.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeSnapshotAttachedInstancesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeSnapshotAttachedInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSnapshotAttachedInstances", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSnapshotAttachedInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSnapshotFiles(self, request):
        """This API is used to query snapshot files.

        :param request: Request instance for DescribeSnapshotFiles.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeSnapshotFilesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeSnapshotFilesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSnapshotFiles", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSnapshotFilesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSnapshotPolicies(self, request):
        """This API is used to query snapshot policies.

        :param request: Request instance for DescribeSnapshotPolicies.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeSnapshotPoliciesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeSnapshotPoliciesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSnapshotPolicies", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSnapshotPoliciesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSubnetResourceDashboard(self, request):
        """This API is used to query the subnet resource.

        :param request: Request instance for DescribeSubnetResourceDashboard.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeSubnetResourceDashboardRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeSubnetResourceDashboardResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSubnetResourceDashboard", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSubnetResourceDashboardResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSubnets(self, request):
        """This API (DescribeSubnets) is used to query the list of subnets.

        :param request: Request instance for DescribeSubnets.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeSubnetsRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeSubnetsResponse`

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


    def DescribeTaskResult(self, request):
        """This API is used to query the EIP async job execution results.

        :param request: Request instance for DescribeTaskResult.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeTaskResultRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeTaskResultResponse`

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


    def DescribeTrafficPackages(self, request):
        """This API is used to query the details of shared traffic packages.

        :param request: Request instance for DescribeTrafficPackages.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeTrafficPackagesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeTrafficPackagesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTrafficPackages", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTrafficPackagesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeUsedIpAddress(self, request):
        """This API is used to query the IP usage of a subnet or VPC.
        If the IP is occupied, the resource type and ID associated with the are is returned. If the IP is not used, it returns null.

        :param request: Request instance for DescribeUsedIpAddress.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeUsedIpAddressRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeUsedIpAddressResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUsedIpAddress", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUsedIpAddressResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVpcEndPoint(self, request):
        """This API is used to query the endpoint list.

        :param request: Request instance for DescribeVpcEndPoint.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeVpcEndPointRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeVpcEndPointResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVpcEndPoint", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVpcEndPointResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVpcEndPointService(self, request):
        """This API is used to query the endpoint service list.

        :param request: Request instance for DescribeVpcEndPointService.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeVpcEndPointServiceRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeVpcEndPointServiceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVpcEndPointService", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVpcEndPointServiceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVpcEndPointServiceWhiteList(self, request):
        """This API is used to query the endpoint service allowlist.

        :param request: Request instance for DescribeVpcEndPointServiceWhiteList.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeVpcEndPointServiceWhiteListRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeVpcEndPointServiceWhiteListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVpcEndPointServiceWhiteList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVpcEndPointServiceWhiteListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVpcInstances(self, request):
        """This API (DescribeVpcInstances) is used to query a list of VCM instances on VPC.

        :param request: Request instance for DescribeVpcInstances.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeVpcInstancesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeVpcInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVpcInstances", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVpcInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVpcIpv6Addresses(self, request):
        """This API (DescribeVpcIpv6Addresses) is used to query `VPC` `IPv6` information.
        This API is used to query only the information of `IPv6` addresses that are already in use. When querying IPs that have not yet been used, this API will not report an error, but the IPs will not appear in the returned results.

        :param request: Request instance for DescribeVpcIpv6Addresses.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeVpcIpv6AddressesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeVpcIpv6AddressesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVpcIpv6Addresses", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVpcIpv6AddressesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVpcPrivateIpAddresses(self, request):
        """This API (DescribeVpcPrivateIpAddresses) is used to query the private IP information of a VPC.<br />
        This API is used to query only the information of IP addresses that are already in use. When querying IPs that have not yet been used, this API will not report an error, but the IPs will not appear in the returned results.

        :param request: Request instance for DescribeVpcPrivateIpAddresses.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeVpcPrivateIpAddressesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeVpcPrivateIpAddressesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVpcPrivateIpAddresses", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVpcPrivateIpAddressesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVpcResourceDashboard(self, request):
        """View VPC resources.

        :param request: Request instance for DescribeVpcResourceDashboard.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeVpcResourceDashboardRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeVpcResourceDashboardResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVpcResourceDashboard", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVpcResourceDashboardResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVpcTaskResult(self, request):
        """This API is used to query the execution result of a VPC task.

        :param request: Request instance for DescribeVpcTaskResult.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeVpcTaskResultRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeVpcTaskResultResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVpcTaskResult", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVpcTaskResultResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVpcs(self, request):
        """This API (DescribeVpcs) is used to query the VPC list.

        :param request: Request instance for DescribeVpcs.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeVpcsRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeVpcsResponse`

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


    def DescribeVpnConnections(self, request):
        """This API is used to used to query the list of VPN tunnels.

        :param request: Request instance for DescribeVpnConnections.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeVpnConnectionsRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeVpnConnectionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVpnConnections", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVpnConnectionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVpnGatewayCcnRoutes(self, request):
        """This API is used to query VPN gateway-based CCN routes.

        :param request: Request instance for DescribeVpnGatewayCcnRoutes.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeVpnGatewayCcnRoutesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeVpnGatewayCcnRoutesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVpnGatewayCcnRoutes", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVpnGatewayCcnRoutesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVpnGatewayRoutes(self, request):
        """This API is used to query VPN gateway routes.

        :param request: Request instance for DescribeVpnGatewayRoutes.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeVpnGatewayRoutesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeVpnGatewayRoutesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVpnGatewayRoutes", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVpnGatewayRoutesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVpnGateways(self, request):
        """This API (DescribeVpnGateways) is used to query the VPN gateway list.

        :param request: Request instance for DescribeVpnGateways.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeVpnGatewaysRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeVpnGatewaysResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVpnGateways", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVpnGatewaysResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DetachCcnInstances(self, request):
        """This API (DetachCcnInstances) is used to unbind a specified network instance from a CCN instance.<br />
        After unbinding the network instance, the corresponding routing policy will also be deleted.

        :param request: Request instance for DetachCcnInstances.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DetachCcnInstancesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DetachCcnInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DetachCcnInstances", params, headers=headers)
            response = json.loads(body)
            model = models.DetachCcnInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DetachClassicLinkVpc(self, request):
        """This API is used to delete a Classiclink.
        >?This API is async. You can call the [`DescribeVpcTaskResult`](https://intl.cloud.tencent.com/document/api/215/59037?from_cn_redirect=1) API to query the task result. When the task is completed, you can continue other tasks.
        >

        :param request: Request instance for DetachClassicLinkVpc.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DetachClassicLinkVpcRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DetachClassicLinkVpcResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DetachClassicLinkVpc", params, headers=headers)
            response = json.loads(body)
            model = models.DetachClassicLinkVpcResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DetachNetworkInterface(self, request):
        """This API is used to unbind an ENI from a CVM.
        This API is completed asynchronously. If you need to query the execution result of an async task, please use the `RequestId` returned by this API to poll the `DescribeVpcTaskResult` API.

        :param request: Request instance for DetachNetworkInterface.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DetachNetworkInterfaceRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DetachNetworkInterfaceResponse`

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


    def DetachSnapshotInstances(self, request):
        """This API is used to disassociate a snapshot policy with instances.

        :param request: Request instance for DetachSnapshotInstances.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DetachSnapshotInstancesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DetachSnapshotInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DetachSnapshotInstances", params, headers=headers)
            response = json.loads(body)
            model = models.DetachSnapshotInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DisableCcnRoutes(self, request):
        """This API (DisableCcnRoutes) is used to disable CCN routes that are already enabled.

        :param request: Request instance for DisableCcnRoutes.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DisableCcnRoutesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DisableCcnRoutesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DisableCcnRoutes", params, headers=headers)
            response = json.loads(body)
            model = models.DisableCcnRoutesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DisableFlowLogs(self, request):
        """This API is used to disable flow log.

        :param request: Request instance for DisableFlowLogs.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DisableFlowLogsRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DisableFlowLogsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DisableFlowLogs", params, headers=headers)
            response = json.loads(body)
            model = models.DisableFlowLogsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DisableGatewayFlowMonitor(self, request):
        """This API is used to disable gateway traffic monitor.

        :param request: Request instance for DisableGatewayFlowMonitor.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DisableGatewayFlowMonitorRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DisableGatewayFlowMonitorResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DisableGatewayFlowMonitor", params, headers=headers)
            response = json.loads(body)
            model = models.DisableGatewayFlowMonitorResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DisableRoutes(self, request):
        """This API is used to disable enabled subnet routes.

        :param request: Request instance for DisableRoutes.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DisableRoutesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DisableRoutesResponse`

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


    def DisableSnapshotPolicies(self, request):
        """This API is used to disable specified snapshot policies.

        :param request: Request instance for DisableSnapshotPolicies.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DisableSnapshotPoliciesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DisableSnapshotPoliciesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DisableSnapshotPolicies", params, headers=headers)
            response = json.loads(body)
            model = models.DisableSnapshotPoliciesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DisassociateAddress(self, request):
        """This API is used to unbind an [Elastic IP](https://intl.cloud.tencent.com/document/product/213/1941?from_cn_redirect=1) (EIP for short).
        * This API supports unbinding an EIP from CVM instances and ENIs.
        * This API does not support unbinding an EIP from a NAT Gateway. To unbind an EIP from a NAT Gateway, use the [`DisassociateNatGatewayAddress`](https://intl.cloud.tencent.com/document/api/215/36716?from_cn_redirect=1) API.
        * Only EIPs in BIND or BIND_ENI status can be unbound.
        * Blocked EIPs cannot be unbound.

        :param request: Request instance for DisassociateAddress.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DisassociateAddressRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DisassociateAddressResponse`

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


    def DisassociateDirectConnectGatewayNatGateway(self, request):
        """This API is used to unbind a direct connect gateway from a NAT Gateway. After unbinding, the direct connect gateway cannot access internet through the NAT Gateway.

        :param request: Request instance for DisassociateDirectConnectGatewayNatGateway.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DisassociateDirectConnectGatewayNatGatewayRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DisassociateDirectConnectGatewayNatGatewayResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DisassociateDirectConnectGatewayNatGateway", params, headers=headers)
            response = json.loads(body)
            model = models.DisassociateDirectConnectGatewayNatGatewayResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DisassociateIPv6Address(self, request):
        """This API is used to unbind an EIPv6 instance.

        - You can unbind EIPv6 instances bound to Cloud Virtual Machine (CVM) or Elastic Network Interface (ENI).
        - Only EIPv6 instances in BIND or BIND_ENI status can be unbound.

        :param request: Request instance for DisassociateIPv6Address.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DisassociateIPv6AddressRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DisassociateIPv6AddressResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DisassociateIPv6Address", params, headers=headers)
            response = json.loads(body)
            model = models.DisassociateIPv6AddressResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DisassociateNatGatewayAddress(self, request):
        """This API is used to unbind an EIP from a NAT gateway.

        :param request: Request instance for DisassociateNatGatewayAddress.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DisassociateNatGatewayAddressRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DisassociateNatGatewayAddressResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DisassociateNatGatewayAddress", params, headers=headers)
            response = json.loads(body)
            model = models.DisassociateNatGatewayAddressResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DisassociateNetworkAclSubnets(self, request):
        """This API is used to disassociate a network ACL from subnets in a VPC instance.

        :param request: Request instance for DisassociateNetworkAclSubnets.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DisassociateNetworkAclSubnetsRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DisassociateNetworkAclSubnetsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DisassociateNetworkAclSubnets", params, headers=headers)
            response = json.loads(body)
            model = models.DisassociateNetworkAclSubnetsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DisassociateNetworkInterfaceSecurityGroups(self, request):
        """This API (DisassociateNetworkInterfaceSecurityGroups) is used to detach (or fully detach if possible) a security group from an ENI.

        :param request: Request instance for DisassociateNetworkInterfaceSecurityGroups.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DisassociateNetworkInterfaceSecurityGroupsRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DisassociateNetworkInterfaceSecurityGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DisassociateNetworkInterfaceSecurityGroups", params, headers=headers)
            response = json.loads(body)
            model = models.DisassociateNetworkInterfaceSecurityGroupsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DisassociateVpcEndPointSecurityGroups(self, request):
        """This API is used to unbind an endpoint from a security group.

        :param request: Request instance for DisassociateVpcEndPointSecurityGroups.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DisassociateVpcEndPointSecurityGroupsRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DisassociateVpcEndPointSecurityGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DisassociateVpcEndPointSecurityGroups", params, headers=headers)
            response = json.loads(body)
            model = models.DisassociateVpcEndPointSecurityGroupsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DownloadCustomerGatewayConfiguration(self, request):
        """This API is used to download VPN tunnel configurations.

        :param request: Request instance for DownloadCustomerGatewayConfiguration.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DownloadCustomerGatewayConfigurationRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DownloadCustomerGatewayConfigurationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DownloadCustomerGatewayConfiguration", params, headers=headers)
            response = json.loads(body)
            model = models.DownloadCustomerGatewayConfigurationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def EnableCcnRoutes(self, request):
        """This API (EnableCcnRoutes) is used to enable CCN routes that are already added.<br />
        This API is used to verify whether there will be conflict with an existing route after a CCN route is enabled. If there is a conflict, the route will not be enabled, and the process will fail. When a conflict occurs, you must disable the conflicting route before you can enable the desired route.

        :param request: Request instance for EnableCcnRoutes.
        :type request: :class:`tencentcloud.vpc.v20170312.models.EnableCcnRoutesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.EnableCcnRoutesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("EnableCcnRoutes", params, headers=headers)
            response = json.loads(body)
            model = models.EnableCcnRoutesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def EnableFlowLogs(self, request):
        """This API is used to enable flow log.

        :param request: Request instance for EnableFlowLogs.
        :type request: :class:`tencentcloud.vpc.v20170312.models.EnableFlowLogsRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.EnableFlowLogsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("EnableFlowLogs", params, headers=headers)
            response = json.loads(body)
            model = models.EnableFlowLogsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def EnableGatewayFlowMonitor(self, request):
        """This API is used to enable gateway traffic monitor.

        :param request: Request instance for EnableGatewayFlowMonitor.
        :type request: :class:`tencentcloud.vpc.v20170312.models.EnableGatewayFlowMonitorRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.EnableGatewayFlowMonitorResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("EnableGatewayFlowMonitor", params, headers=headers)
            response = json.loads(body)
            model = models.EnableGatewayFlowMonitorResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def EnableRoutes(self, request):
        """This API is used to enable disabled subnet routes.<br />
        The API is used to verify whether the enabled route conflicts with existing routes. If they conflict, the new route cannot be enabled and will result in a failure. When a route conflict occurs, you need to first disable the conflicting route before you can enable the new one.

        :param request: Request instance for EnableRoutes.
        :type request: :class:`tencentcloud.vpc.v20170312.models.EnableRoutesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.EnableRoutesResponse`

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


    def EnableSnapshotPolicies(self, request):
        """This API is used to enable specified snapshot policies.

        :param request: Request instance for EnableSnapshotPolicies.
        :type request: :class:`tencentcloud.vpc.v20170312.models.EnableSnapshotPoliciesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.EnableSnapshotPoliciesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("EnableSnapshotPolicies", params, headers=headers)
            response = json.loads(body)
            model = models.EnableSnapshotPoliciesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def EnableVpcEndPointConnect(self, request):
        """This API is used to determine whether to accept the request of connecting with an endpoint.

        :param request: Request instance for EnableVpcEndPointConnect.
        :type request: :class:`tencentcloud.vpc.v20170312.models.EnableVpcEndPointConnectRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.EnableVpcEndPointConnectResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("EnableVpcEndPointConnect", params, headers=headers)
            response = json.loads(body)
            model = models.EnableVpcEndPointConnectResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GenerateVpnConnectionDefaultHealthCheckIp(self, request):
        """This API is used to get a pair of VPN tunnel health check addresses.

        :param request: Request instance for GenerateVpnConnectionDefaultHealthCheckIp.
        :type request: :class:`tencentcloud.vpc.v20170312.models.GenerateVpnConnectionDefaultHealthCheckIpRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.GenerateVpnConnectionDefaultHealthCheckIpResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GenerateVpnConnectionDefaultHealthCheckIp", params, headers=headers)
            response = json.loads(body)
            model = models.GenerateVpnConnectionDefaultHealthCheckIpResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetCcnRegionBandwidthLimits(self, request):
        """This API is used to query the bandwidth limits of a CCN instance. Monthly-subscribed CCNs only support Inter-region Bandwidth Limits, while the pay-as-you-go CCNs support both the Inter-region Bandwidth Limits and Region Outbound Bandwidth Limits.

        :param request: Request instance for GetCcnRegionBandwidthLimits.
        :type request: :class:`tencentcloud.vpc.v20170312.models.GetCcnRegionBandwidthLimitsRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.GetCcnRegionBandwidthLimitsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetCcnRegionBandwidthLimits", params, headers=headers)
            response = json.loads(body)
            model = models.GetCcnRegionBandwidthLimitsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def HaVipAssociateAddressIp(self, request):
        """This API is used to bind an EIP to an HAVIP. <br />
        This API is completed asynchronously. If you need to query the execution result of an async task, please use the `RequestId` returned by this API to poll the `DescribeVpcTaskResult` API.

        :param request: Request instance for HaVipAssociateAddressIp.
        :type request: :class:`tencentcloud.vpc.v20170312.models.HaVipAssociateAddressIpRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.HaVipAssociateAddressIpResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("HaVipAssociateAddressIp", params, headers=headers)
            response = json.loads(body)
            model = models.HaVipAssociateAddressIpResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def HaVipDisassociateAddressIp(self, request):
        """This API is used to unbind an EIP from an HAVIP. <br />
        This API is completed asynchronously. If you need to query the execution result of an async task, please use the `RequestId` returned by this API to poll the `DescribeVpcTaskResult` API.

        :param request: Request instance for HaVipDisassociateAddressIp.
        :type request: :class:`tencentcloud.vpc.v20170312.models.HaVipDisassociateAddressIpRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.HaVipDisassociateAddressIpResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("HaVipDisassociateAddressIp", params, headers=headers)
            response = json.loads(body)
            model = models.HaVipDisassociateAddressIpResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def InquirePriceCreateDirectConnectGateway(self, request):
        """This API is used to query the price of creating a direct connect gateway.

        :param request: Request instance for InquirePriceCreateDirectConnectGateway.
        :type request: :class:`tencentcloud.vpc.v20170312.models.InquirePriceCreateDirectConnectGatewayRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.InquirePriceCreateDirectConnectGatewayResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("InquirePriceCreateDirectConnectGateway", params, headers=headers)
            response = json.loads(body)
            model = models.InquirePriceCreateDirectConnectGatewayResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def InquiryPriceAllocateAddresses(self, request):
        """This API (InquiryPriceAllocateAddresses) is used to query the price of purchasing EIPs.

        :param request: Request instance for InquiryPriceAllocateAddresses.
        :type request: :class:`tencentcloud.vpc.v20170312.models.InquiryPriceAllocateAddressesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.InquiryPriceAllocateAddressesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("InquiryPriceAllocateAddresses", params, headers=headers)
            response = json.loads(body)
            model = models.InquiryPriceAllocateAddressesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def InquiryPriceModifyAddressesBandwidth(self, request):
        """This API is used to query the price of modifying EIP bandwidth.

        :param request: Request instance for InquiryPriceModifyAddressesBandwidth.
        :type request: :class:`tencentcloud.vpc.v20170312.models.InquiryPriceModifyAddressesBandwidthRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.InquiryPriceModifyAddressesBandwidthResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("InquiryPriceModifyAddressesBandwidth", params, headers=headers)
            response = json.loads(body)
            model = models.InquiryPriceModifyAddressesBandwidthResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def InquiryPriceRenewAddresses(self, request):
        """This API (InquiryPriceRenewAddresses) is used to query the price of renewing prepaid EIPs.

        :param request: Request instance for InquiryPriceRenewAddresses.
        :type request: :class:`tencentcloud.vpc.v20170312.models.InquiryPriceRenewAddressesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.InquiryPriceRenewAddressesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("InquiryPriceRenewAddresses", params, headers=headers)
            response = json.loads(body)
            model = models.InquiryPriceRenewAddressesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def InquiryPriceRenewVpnGateway(self, request):
        """This API (InquiryPriceRenewVpnGateway) is used to query the price for VPN gateway renewal. Currently, only querying prices for IPSEC-type gateways is supported.

        :param request: Request instance for InquiryPriceRenewVpnGateway.
        :type request: :class:`tencentcloud.vpc.v20170312.models.InquiryPriceRenewVpnGatewayRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.InquiryPriceRenewVpnGatewayResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("InquiryPriceRenewVpnGateway", params, headers=headers)
            response = json.loads(body)
            model = models.InquiryPriceRenewVpnGatewayResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def InquiryPriceResetVpnGatewayInternetMaxBandwidth(self, request):
        """This API (InquiryPriceResetVpnGatewayInternetMaxBandwidth) is used to query the price for adjusting the bandwidth cap of a VPN gateway.

        :param request: Request instance for InquiryPriceResetVpnGatewayInternetMaxBandwidth.
        :type request: :class:`tencentcloud.vpc.v20170312.models.InquiryPriceResetVpnGatewayInternetMaxBandwidthRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.InquiryPriceResetVpnGatewayInternetMaxBandwidthResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("InquiryPriceResetVpnGatewayInternetMaxBandwidth", params, headers=headers)
            response = json.loads(body)
            model = models.InquiryPriceResetVpnGatewayInternetMaxBandwidthResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def MigrateNetworkInterface(self, request):
        """This API is used to migrate ENIs.
        This API is completed asynchronously. If you need to query the execution result of an async task, please use the `RequestId` returned by this API to poll the `DescribeVpcTaskResult` API.

        :param request: Request instance for MigrateNetworkInterface.
        :type request: :class:`tencentcloud.vpc.v20170312.models.MigrateNetworkInterfaceRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.MigrateNetworkInterfaceResponse`

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
        """This API is used to migrate the private IPs between ENIs.
        * Note that primary IPs cannot be migrated.
        * The source and destination ENI must be within the same subnet.

        This API is completed asynchronously. If you need to query the execution result of an async task, please use the `RequestId` returned by this API to poll the `DescribeVpcTaskResult` API.

        :param request: Request instance for MigratePrivateIpAddress.
        :type request: :class:`tencentcloud.vpc.v20170312.models.MigratePrivateIpAddressRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.MigratePrivateIpAddressResponse`

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
        """This API (ModifyAddressAttribute) is used to modify the name of an [Elastic IP](https://intl.cloud.tencent.com/document/product/213/1941?from_cn_redirect=1).

        :param request: Request instance for ModifyAddressAttribute.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyAddressAttributeRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyAddressAttributeResponse`

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


    def ModifyAddressInternetChargeType(self, request):
        """This API is used to adjust the network billing mode of an EIP. Please note that it's available to users whose network fees are billed on IPs but not CVMs.
        * The network billing mode can be switched between `BANDWIDTH_PREPAID_BY_MONTH` and `TRAFFIC_POSTPAID_BY_HOUR`.
        * The network billing mode for each EIP be changed for up to twice.

        :param request: Request instance for ModifyAddressInternetChargeType.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyAddressInternetChargeTypeRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyAddressInternetChargeTypeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAddressInternetChargeType", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAddressInternetChargeTypeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAddressTemplateAttribute(self, request):
        """This API (ModifyAddressTemplateAttribute) is used to modify an IP address template.

        :param request: Request instance for ModifyAddressTemplateAttribute.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyAddressTemplateAttributeRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyAddressTemplateAttributeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAddressTemplateAttribute", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAddressTemplateAttributeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAddressTemplateGroupAttribute(self, request):
        """This API (ModifyAddressTemplateGroupAttribute) is used to modify an IP address template group.

        :param request: Request instance for ModifyAddressTemplateGroupAttribute.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyAddressTemplateGroupAttributeRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyAddressTemplateGroupAttributeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAddressTemplateGroupAttribute", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAddressTemplateGroupAttributeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAddressesBandwidth(self, request):
        """This API is used to adjust the bandwidth of [Elastic IP](https://intl.cloud.tencent.com/document/product/213/1941?from_cn_redirect=1), including EIP billed on a pay-as-you-go, monthly subscription, and bandwidth package basis.

        :param request: Request instance for ModifyAddressesBandwidth.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyAddressesBandwidthRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyAddressesBandwidthResponse`

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


    def ModifyAddressesRenewFlag(self, request):
        """This API is used to adjust the renewal flag for the monthly subscription EIP.

        :param request: Request instance for ModifyAddressesRenewFlag.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyAddressesRenewFlagRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyAddressesRenewFlagResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAddressesRenewFlag", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAddressesRenewFlagResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAssistantCidr(self, request):
        """This API is used to batch modify (add or delete) secondary CIDR blocks.

        :param request: Request instance for ModifyAssistantCidr.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyAssistantCidrRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyAssistantCidrResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAssistantCidr", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAssistantCidrResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyBandwidthPackageAttribute(self, request):
        """This API is used to modify the attributes of a bandwidth package, including the bandwidth package name, and so on.

        :param request: Request instance for ModifyBandwidthPackageAttribute.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyBandwidthPackageAttributeRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyBandwidthPackageAttributeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyBandwidthPackageAttribute", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyBandwidthPackageAttributeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyBandwidthPackageBandwidth(self, request):
        """This API is used to adjust the bandwidth of a [bandwidth package](https://www.tencentcloud.com/document/product/684/15245).

        :param request: Request instance for ModifyBandwidthPackageBandwidth.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyBandwidthPackageBandwidthRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyBandwidthPackageBandwidthResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyBandwidthPackageBandwidth", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyBandwidthPackageBandwidthResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyCcnAttachedInstancesAttribute(self, request):
        """This API is used to modify CCN-associated instance attributes. Currently, only the `description` can be modified.

        :param request: Request instance for ModifyCcnAttachedInstancesAttribute.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyCcnAttachedInstancesAttributeRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyCcnAttachedInstancesAttributeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyCcnAttachedInstancesAttribute", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyCcnAttachedInstancesAttributeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyCcnAttribute(self, request):
        """This API (ModifyCcnAttribute) is used to modify CCN attributes.

        :param request: Request instance for ModifyCcnAttribute.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyCcnAttributeRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyCcnAttributeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyCcnAttribute", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyCcnAttributeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyCcnRegionBandwidthLimitsType(self, request):
        """This API is used to modify the bandwidth limit policy of a postpaid CCN instance.

        :param request: Request instance for ModifyCcnRegionBandwidthLimitsType.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyCcnRegionBandwidthLimitsTypeRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyCcnRegionBandwidthLimitsTypeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyCcnRegionBandwidthLimitsType", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyCcnRegionBandwidthLimitsTypeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyCustomerGatewayAttribute(self, request):
        """This API (ModifyCustomerGatewayAttribute) is used to modify the customer gateway information.

        :param request: Request instance for ModifyCustomerGatewayAttribute.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyCustomerGatewayAttributeRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyCustomerGatewayAttributeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyCustomerGatewayAttribute", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyCustomerGatewayAttributeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDirectConnectGatewayAttribute(self, request):
        """This API is used to modify the attributes of a direct connect gateway.

        :param request: Request instance for ModifyDirectConnectGatewayAttribute.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyDirectConnectGatewayAttributeRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyDirectConnectGatewayAttributeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDirectConnectGatewayAttribute", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDirectConnectGatewayAttributeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyFlowLogAttribute(self, request):
        """This API is used to modify the attributes of a flow log.

        :param request: Request instance for ModifyFlowLogAttribute.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyFlowLogAttributeRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyFlowLogAttributeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyFlowLogAttribute", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyFlowLogAttributeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyGatewayFlowQos(self, request):
        """This API is used to adjust the bandwidth limit of a gateway.

        :param request: Request instance for ModifyGatewayFlowQos.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyGatewayFlowQosRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyGatewayFlowQosResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyGatewayFlowQos", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyGatewayFlowQosResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyHaVipAttribute(self, request):
        """This API (ModifyHaVipAttribute) is used to modify HAVIP attributes.

        :param request: Request instance for ModifyHaVipAttribute.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyHaVipAttributeRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyHaVipAttributeResponse`

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


    def ModifyIPv6AddressesAttributes(self, request):
        """This API is used to modify the name of an EIPv6 instance.

        - You can modify the name of both EIPv6 and traditional EIPv6 instances.

        :param request: Request instance for ModifyIPv6AddressesAttributes.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyIPv6AddressesAttributesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyIPv6AddressesAttributesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyIPv6AddressesAttributes", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyIPv6AddressesAttributesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyIPv6AddressesBandwidth(self, request):
        """This API is used to modify the bandwidth cap of an EIPv6 instance.

        :param request: Request instance for ModifyIPv6AddressesBandwidth.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyIPv6AddressesBandwidthRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyIPv6AddressesBandwidthResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyIPv6AddressesBandwidth", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyIPv6AddressesBandwidthResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyIp6AddressesBandwidth(self, request):
        """This API is used to adjust the bandwidth limit of a classic elastic public IPv6 instance.

        - You can adjust the bandwidth limit of only classic elastic public IPv6 instances.
        - To adjust the bandwidth limit of an elastic public IPv6 instance, call the ModifyIPv6AddressesBandwidth API.

        :param request: Request instance for ModifyIp6AddressesBandwidth.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyIp6AddressesBandwidthRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyIp6AddressesBandwidthResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyIp6AddressesBandwidth", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyIp6AddressesBandwidthResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyIpv6AddressesAttribute(self, request):
        """This API (ModifyIpv6AddressesAttribute) is used to modify the private IPv6 address attributes of an ENI.

        :param request: Request instance for ModifyIpv6AddressesAttribute.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyIpv6AddressesAttributeRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyIpv6AddressesAttributeResponse`

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


    def ModifyLocalGateway(self, request):
        """This API is used to modify the local gateway of a CDC instance.

        :param request: Request instance for ModifyLocalGateway.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyLocalGatewayRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyLocalGatewayResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyLocalGateway", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyLocalGatewayResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyNatGatewayAttribute(self, request):
        """This API is used to modify the attributes of a NAT gateway.

        :param request: Request instance for ModifyNatGatewayAttribute.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyNatGatewayAttributeRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyNatGatewayAttributeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyNatGatewayAttribute", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyNatGatewayAttributeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyNatGatewayDestinationIpPortTranslationNatRule(self, request):
        """This API is used to modify the port forwarding rule of a NAT gateway.

        :param request: Request instance for ModifyNatGatewayDestinationIpPortTranslationNatRule.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyNatGatewayDestinationIpPortTranslationNatRuleRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyNatGatewayDestinationIpPortTranslationNatRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyNatGatewayDestinationIpPortTranslationNatRule", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyNatGatewayDestinationIpPortTranslationNatRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyNatGatewaySourceIpTranslationNatRule(self, request):
        """This API is used to modify a NAT gateway's SNAT forwarding rules.

        :param request: Request instance for ModifyNatGatewaySourceIpTranslationNatRule.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyNatGatewaySourceIpTranslationNatRuleRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyNatGatewaySourceIpTranslationNatRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyNatGatewaySourceIpTranslationNatRule", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyNatGatewaySourceIpTranslationNatRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyNetDetect(self, request):
        """This API (ModifyNetDetect) is used to modify network detection parameters.

        :param request: Request instance for ModifyNetDetect.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyNetDetectRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyNetDetectResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyNetDetect", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyNetDetectResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyNetworkAclAttribute(self, request):
        """This API is used to modify the attributes of a network ACL.

        :param request: Request instance for ModifyNetworkAclAttribute.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyNetworkAclAttributeRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyNetworkAclAttributeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyNetworkAclAttribute", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyNetworkAclAttributeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyNetworkAclEntries(self, request):
        """This API is used to modify (add or delete) the inbound and outbound rules of a network ACL. In `NetworkAclEntrySet` parameters,
        * Passing in the new inbound/outbound rules will reset the original rules.
        * Passing in the inbound rules will only reset the original inbound rules and not affect the original outbound rules, and vice versa.

        :param request: Request instance for ModifyNetworkAclEntries.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyNetworkAclEntriesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyNetworkAclEntriesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyNetworkAclEntries", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyNetworkAclEntriesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyNetworkAclQuintupleEntries(self, request):
        """This API is used to modify the in/outbound rules of the network ACL quintuple. In the `NetworkAclQuintupleEntrySet` parameters, `NetworkAclQuintupleEntryId` is required for `NetworkAclQuintupleEntry`.

        :param request: Request instance for ModifyNetworkAclQuintupleEntries.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyNetworkAclQuintupleEntriesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyNetworkAclQuintupleEntriesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyNetworkAclQuintupleEntries", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyNetworkAclQuintupleEntriesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyNetworkInterfaceAttribute(self, request):
        """This API (ModifyNetworkInterfaceAttribute) is used to modify ENI attributes.

        :param request: Request instance for ModifyNetworkInterfaceAttribute.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyNetworkInterfaceAttributeRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyNetworkInterfaceAttributeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyNetworkInterfaceAttribute", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyNetworkInterfaceAttributeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyPrivateIpAddressesAttribute(self, request):
        """This API (ModifyPrivateIpAddressesAttribute) is used to modify the private IP attributes of an ENI.

        :param request: Request instance for ModifyPrivateIpAddressesAttribute.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyPrivateIpAddressesAttributeRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyPrivateIpAddressesAttributeResponse`

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


    def ModifyReserveIpAddress(self, request):
        """This API is used to modify a reserved private IP address.

        :param request: Request instance for ModifyReserveIpAddress.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyReserveIpAddressRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyReserveIpAddressResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyReserveIpAddress", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyReserveIpAddressResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyRouteTableAttribute(self, request):
        """This API (ModifyRouteTableAttribute) is used to modify the attributes of a route table.

        :param request: Request instance for ModifyRouteTableAttribute.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyRouteTableAttributeRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyRouteTableAttributeResponse`

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
        """This API (ModifySecurityGroupAttribute) is used to modify the attributes of a security group (SecurityGroupPolicy).

        :param request: Request instance for ModifySecurityGroupAttribute.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifySecurityGroupAttributeRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifySecurityGroupAttributeResponse`

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
        """This API is used to reset the `Egress` and `Ingress` rules (SecurityGroupPolicy) of a security group.

        <ul>
        <li>This API does not support custom indexes <code>PolicyIndex</code>. </li>
        <li>For <code>SecurityGroupPolicySet</code> parameter,<ul> <ul>
        	<li>If <code>SecurityGroupPolicySet.Version</code> is set to `0`, all policies will be cleared, and <code>Egress</code> and <code>Ingress</code> will be ignored. </li>
        	<li>If <code>SecurityGroupPolicySet.Version</code> is not set to `0`, add <code>Egress</code> and <code>Ingress</code> policies: <ul>
        		<li><code>Protocol</code>: <code>TCP</code>, <code>UDP</code>, <code>ICMP</code>, <code>ICMPV6</code>, <code>GRE</code>, or <code>ALL</code>. </li>
        		<li><code>CidrBlock</code>: a CIDR block in the correct format. In the classic network, even if the CIDR block specified in <code>CidrBlock</code> contains the Tencent Cloud private IPs that are not using for CVMs under your Tencent Cloud account, it does not mean this policy allows you to access those resources. The network isolation policies between tenants take priority over the private network policies in security groups. </li>
        		<li><code>Ipv6CidrBlock</code>: an IPv6 CIDR block in the correct format. In the classic network, even if the CIDR block specified in <code>Ipv6CidrBlock</code> contains the Tencent Cloud private IPv6 addresses that are not using for CVMs under your Tencent Cloud account, it does not mean this policy allows you to access those resources. The network isolation policies between tenants take priority over the private network policies in security groups. </li>
        		<li><code>SecurityGroupId</code>: ID of the security group. It can be the ID of a security group to be modified, or the ID of another security group in the same project. All private IPs of all CVMs under the security group will be covered. If this field is used, the policy will automatically change according to the CVM associated with the group ID while being used to match network messages. You don't need to change it manually. </li>
        		<li><code>Port</code>: a single port number such as 80, or a port range in the format of '8000-8010'.  You may use this field only if the <code>Protocol</code> field takes the value <code>TCP</code> or <code>UDP</code>. </li>
        		<li><code>Action</code>: only allows <code>ACCEPT</code> or <code>DROP</code>. </li>
        		<li><code>CidrBlock</code>, <code>Ipv6CidrBlock</code>, <code>SecurityGroupId</code>, and <code>AddressTemplate</code> are mutually exclusive. <code>Protocol</code> + <code>Port</code> and <code>ServiceTemplate</code> are mutually exclusive.</li> </li>
        </ul></li></ul></li>
        </ul>

        :param request: Request instance for ModifySecurityGroupPolicies.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifySecurityGroupPoliciesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifySecurityGroupPoliciesResponse`

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


    def ModifyServiceTemplateAttribute(self, request):
        """This API (ModifyServiceTemplateAttribute) is used to modify a protocol port template.

        :param request: Request instance for ModifyServiceTemplateAttribute.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyServiceTemplateAttributeRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyServiceTemplateAttributeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyServiceTemplateAttribute", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyServiceTemplateAttributeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyServiceTemplateGroupAttribute(self, request):
        """This API (ModifyServiceTemplateGroupAttribute) is used to modify a protocol port template group.

        :param request: Request instance for ModifyServiceTemplateGroupAttribute.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyServiceTemplateGroupAttributeRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyServiceTemplateGroupAttributeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyServiceTemplateGroupAttribute", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyServiceTemplateGroupAttributeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifySnapshotPolicies(self, request):
        """This API is used to modify specified snapshot policies.

        :param request: Request instance for ModifySnapshotPolicies.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifySnapshotPoliciesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifySnapshotPoliciesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifySnapshotPolicies", params, headers=headers)
            response = json.loads(body)
            model = models.ModifySnapshotPoliciesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifySubnetAttribute(self, request):
        """This API (ModifySubnetAttribute) is used to modify subnet attributes.

        :param request: Request instance for ModifySubnetAttribute.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifySubnetAttributeRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifySubnetAttributeResponse`

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


    def ModifyTemplateMember(self, request):
        """This API is used to modify a parameter template of the IP address, protocol port, IP address group, or protocol port group type.

        :param request: Request instance for ModifyTemplateMember.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyTemplateMemberRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyTemplateMemberResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyTemplateMember", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyTemplateMemberResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyVpcAttribute(self, request):
        """This API (ModifyVpcAttribute) is used to modify VPC attributes.

        :param request: Request instance for ModifyVpcAttribute.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyVpcAttributeRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyVpcAttributeResponse`

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


    def ModifyVpcEndPointAttribute(self, request):
        """This API is used to modify endpoint attributes.

        :param request: Request instance for ModifyVpcEndPointAttribute.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyVpcEndPointAttributeRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyVpcEndPointAttributeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyVpcEndPointAttribute", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyVpcEndPointAttributeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyVpcEndPointServiceAttribute(self, request):
        """This API is used to modify the VPC endpoint service attributes.


        :param request: Request instance for ModifyVpcEndPointServiceAttribute.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyVpcEndPointServiceAttributeRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyVpcEndPointServiceAttributeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyVpcEndPointServiceAttribute", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyVpcEndPointServiceAttributeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyVpcEndPointServiceWhiteList(self, request):
        """This API is used to modify the attributes of the endpoint service allowlist.

        :param request: Request instance for ModifyVpcEndPointServiceWhiteList.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyVpcEndPointServiceWhiteListRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyVpcEndPointServiceWhiteListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyVpcEndPointServiceWhiteList", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyVpcEndPointServiceWhiteListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyVpnConnectionAttribute(self, request):
        """This API (ModifyVpnConnectionAttribute) is used to modify VPN tunnels.

        :param request: Request instance for ModifyVpnConnectionAttribute.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyVpnConnectionAttributeRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyVpnConnectionAttributeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyVpnConnectionAttribute", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyVpnConnectionAttributeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyVpnGatewayAttribute(self, request):
        """This API (ModifyVpnGatewayAttribute) is used to modify the attributes of VPN gateways.

        :param request: Request instance for ModifyVpnGatewayAttribute.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyVpnGatewayAttributeRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyVpnGatewayAttributeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyVpnGatewayAttribute", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyVpnGatewayAttributeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyVpnGatewayCcnRoutes(self, request):
        """This API is used to modify VPN gateway-based CCN routes.

        :param request: Request instance for ModifyVpnGatewayCcnRoutes.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyVpnGatewayCcnRoutesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyVpnGatewayCcnRoutesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyVpnGatewayCcnRoutes", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyVpnGatewayCcnRoutesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyVpnGatewayRoutes(self, request):
        """This API is used to modify VPN gateway routes.

        :param request: Request instance for ModifyVpnGatewayRoutes.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyVpnGatewayRoutesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyVpnGatewayRoutesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyVpnGatewayRoutes", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyVpnGatewayRoutesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def NotifyRoutes(self, request):
        """This API is used to publish a route to CCN. This can also be done by clicking "Publish to CCN" in the operation column on the page of route table list.

        :param request: Request instance for NotifyRoutes.
        :type request: :class:`tencentcloud.vpc.v20170312.models.NotifyRoutesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.NotifyRoutesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("NotifyRoutes", params, headers=headers)
            response = json.loads(body)
            model = models.NotifyRoutesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RefreshDirectConnectGatewayRouteToNatGateway(self, request):
        """This API is used to refresh the route between a NAT gateway and  Direct Connect and update the associated route table.

        :param request: Request instance for RefreshDirectConnectGatewayRouteToNatGateway.
        :type request: :class:`tencentcloud.vpc.v20170312.models.RefreshDirectConnectGatewayRouteToNatGatewayRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.RefreshDirectConnectGatewayRouteToNatGatewayResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RefreshDirectConnectGatewayRouteToNatGateway", params, headers=headers)
            response = json.loads(body)
            model = models.RefreshDirectConnectGatewayRouteToNatGatewayResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RejectAttachCcnInstances(self, request):
        """This API (RejectAttachCcnInstances) is used to reject association operations when instances are associated across accounts for the CCN owner.

        :param request: Request instance for RejectAttachCcnInstances.
        :type request: :class:`tencentcloud.vpc.v20170312.models.RejectAttachCcnInstancesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.RejectAttachCcnInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RejectAttachCcnInstances", params, headers=headers)
            response = json.loads(body)
            model = models.RejectAttachCcnInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ReleaseAddresses(self, request):
        """This API (ReleaseAddresses) is used to release one or multiple [Elastic IPs](https://intl.cloud.tencent.com/document/product/213/1941?from_cn_redirect=1).
        * This operation is irreversible. Once you release an EIP, the IP address associated with the EIP no longer belongs to you.
        * Only EIPs in UNBIND status can be released.

        :param request: Request instance for ReleaseAddresses.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ReleaseAddressesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ReleaseAddressesResponse`

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


    def ReleaseIPv6Addresses(self, request):
        """This API is used to release one or more EIPv6 instances.

        - You can release the obtained EIPv6 instances. To use them again, please reapply.
        - Only EIPv6 instances in UNBIND status can be released.

        :param request: Request instance for ReleaseIPv6Addresses.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ReleaseIPv6AddressesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ReleaseIPv6AddressesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ReleaseIPv6Addresses", params, headers=headers)
            response = json.loads(body)
            model = models.ReleaseIPv6AddressesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ReleaseIp6AddressesBandwidth(self, request):
        """This API is used to release the IPv6 public network bandwidth of classic elastic public IPv6 instances.

        - Classic elastic public IPv6 addresses still have the IPv6 private network communication capability after the public network bandwidth is released.
        - To allocate IPV6 public network bandwidth, call the AllocateIp6AddressesBandwidth API.

        :param request: Request instance for ReleaseIp6AddressesBandwidth.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ReleaseIp6AddressesBandwidthRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ReleaseIp6AddressesBandwidthResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ReleaseIp6AddressesBandwidth", params, headers=headers)
            response = json.loads(body)
            model = models.ReleaseIp6AddressesBandwidthResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RemoveBandwidthPackageResources(self, request):
        """This API is used to delete a bandwidth package resource, including [Elastic IP](https://intl.cloud.tencent.com/document/product/213/1941?from_cn_redirect=1), [Cloud Load Balancer](https://intl.cloud.tencent.com/document/product/214/517?from_cn_redirect=1), and so on.

        :param request: Request instance for RemoveBandwidthPackageResources.
        :type request: :class:`tencentcloud.vpc.v20170312.models.RemoveBandwidthPackageResourcesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.RemoveBandwidthPackageResourcesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RemoveBandwidthPackageResources", params, headers=headers)
            response = json.loads(body)
            model = models.RemoveBandwidthPackageResourcesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RenewVpnGateway(self, request):
        """This API (RenewVpnGateway) is used to renew prepaid (monthly subscription) VPN gateways. Currently, only IPSEC gateways are supported.

        :param request: Request instance for RenewVpnGateway.
        :type request: :class:`tencentcloud.vpc.v20170312.models.RenewVpnGatewayRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.RenewVpnGatewayResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RenewVpnGateway", params, headers=headers)
            response = json.loads(body)
            model = models.RenewVpnGatewayResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ReplaceDirectConnectGatewayCcnRoutes(self, request):
        """This API (ReplaceDirectConnectGatewayCcnRoutes) is used to modify the specified route according to the route ID. Batch modification is supported.

        :param request: Request instance for ReplaceDirectConnectGatewayCcnRoutes.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ReplaceDirectConnectGatewayCcnRoutesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ReplaceDirectConnectGatewayCcnRoutesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ReplaceDirectConnectGatewayCcnRoutes", params, headers=headers)
            response = json.loads(body)
            model = models.ReplaceDirectConnectGatewayCcnRoutesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ReplaceRouteTableAssociation(self, request):
        """This API (ReplaceRouteTableAssociation) is used to modify the route table associated with a subnet.
        * A subnet can only be associated with one route table.

        :param request: Request instance for ReplaceRouteTableAssociation.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ReplaceRouteTableAssociationRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ReplaceRouteTableAssociationResponse`

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
        """This API (ReplaceRoutes) is used to modify a specified routing policy by its ID (RouteId). Batch modification is supported.

        :param request: Request instance for ReplaceRoutes.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ReplaceRoutesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ReplaceRoutesResponse`

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


    def ReplaceSecurityGroupPolicies(self, request):
        """This API is used to batch modify security group policies.
        Policies to modify must be in the same direction. `PolicyIndex` must be specified.

        :param request: Request instance for ReplaceSecurityGroupPolicies.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ReplaceSecurityGroupPoliciesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ReplaceSecurityGroupPoliciesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ReplaceSecurityGroupPolicies", params, headers=headers)
            response = json.loads(body)
            model = models.ReplaceSecurityGroupPoliciesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ReplaceSecurityGroupPolicy(self, request):
        """This API (ReplaceSecurityGroupPolicy) is used to replace a single security group policy (SecurityGroupPolicy).
        Only one policy in a single direction can be replaced in each request, and the PolicyIndex parameter must be specified.

        :param request: Request instance for ReplaceSecurityGroupPolicy.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ReplaceSecurityGroupPolicyRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ReplaceSecurityGroupPolicyResponse`

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


    def ResetAttachCcnInstances(self, request):
        """This API (ResetAttachCcnInstances) is used to re-apply for the association operation when the application for cross-account instance association expires.

        :param request: Request instance for ResetAttachCcnInstances.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ResetAttachCcnInstancesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ResetAttachCcnInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ResetAttachCcnInstances", params, headers=headers)
            response = json.loads(body)
            model = models.ResetAttachCcnInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ResetNatGatewayConnection(self, request):
        """This API is used to adjust concurrent connection cap for the NAT gateway.

        :param request: Request instance for ResetNatGatewayConnection.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ResetNatGatewayConnectionRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ResetNatGatewayConnectionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ResetNatGatewayConnection", params, headers=headers)
            response = json.loads(body)
            model = models.ResetNatGatewayConnectionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ResetRoutes(self, request):
        """This API (ResetRoutes) is used to reset the name of a route table and all its routing policies.<br />
        Note: When this API is called, all routing policies in the current route table are deleted before new routing policies are saved, which may incur network interruption.

        :param request: Request instance for ResetRoutes.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ResetRoutesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ResetRoutesResponse`

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


    def ResetVpnConnection(self, request):
        """The API is used to reset a VPN tunnel.

        :param request: Request instance for ResetVpnConnection.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ResetVpnConnectionRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ResetVpnConnectionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ResetVpnConnection", params, headers=headers)
            response = json.loads(body)
            model = models.ResetVpnConnectionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ResetVpnGatewayInternetMaxBandwidth(self, request):
        """This API is used to adjust the bandwidth cap of a VPN gateway. The adjustment of the VPN gateway bandwidth is limited to [5,100] Mbps and [200,1000] Mbps.

        :param request: Request instance for ResetVpnGatewayInternetMaxBandwidth.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ResetVpnGatewayInternetMaxBandwidthRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ResetVpnGatewayInternetMaxBandwidthResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ResetVpnGatewayInternetMaxBandwidth", params, headers=headers)
            response = json.loads(body)
            model = models.ResetVpnGatewayInternetMaxBandwidthResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ResumeSnapshotInstance(self, request):
        """This API is used to restore security group policies with a backup.

        :param request: Request instance for ResumeSnapshotInstance.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ResumeSnapshotInstanceRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ResumeSnapshotInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ResumeSnapshotInstance", params, headers=headers)
            response = json.loads(body)
            model = models.ResumeSnapshotInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ReturnNormalAddresses(self, request):
        """This API is used to unbind and release public IPs.
        Note: Starting from Dec 15, 2022, CAM authorization is required for a sub-account to call this API. For more details, see [Authorization Guide](https://intl.cloud.tencent.com/document/product/598/34545?from_cn_redirect=1).

        :param request: Request instance for ReturnNormalAddresses.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ReturnNormalAddressesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ReturnNormalAddressesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ReturnNormalAddresses", params, headers=headers)
            response = json.loads(body)
            model = models.ReturnNormalAddressesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SetCcnRegionBandwidthLimits(self, request):
        """This API (SetCcnRegionBandwidthLimits) is used to set the outbound bandwidth cap for CCNs in each region. This API can only set the outbound bandwidth cap for regions in the network instances that have already been associated.

        :param request: Request instance for SetCcnRegionBandwidthLimits.
        :type request: :class:`tencentcloud.vpc.v20170312.models.SetCcnRegionBandwidthLimitsRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.SetCcnRegionBandwidthLimitsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SetCcnRegionBandwidthLimits", params, headers=headers)
            response = json.loads(body)
            model = models.SetCcnRegionBandwidthLimitsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SetVpnGatewaysRenewFlag(self, request):
        """This API is used set the auto-renewal configuration of a VPN gateway.

        :param request: Request instance for SetVpnGatewaysRenewFlag.
        :type request: :class:`tencentcloud.vpc.v20170312.models.SetVpnGatewaysRenewFlagRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.SetVpnGatewaysRenewFlagResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SetVpnGatewaysRenewFlag", params, headers=headers)
            response = json.loads(body)
            model = models.SetVpnGatewaysRenewFlagResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def TransformAddress(self, request):
        """This API is used to convert a common public IP into an [Elastic IP](https://intl.cloud.tencent.com/document/product/213/1941?from_cn_redirect=1) (EIP for short).
        * Tencent Cloud limits the number of times that a user can unbind EIPs and reassign public IPs in each region per day. For more information, see product introduction of [Elastic IP](https://intl.cloud.tencent.com/document/product/213/5733?from_cn_redirect=1). The preceding quota can be obtained through the API [DescribeAddressQuota](https://intl.cloud.tencent.com/document/product/215/16701).

        :param request: Request instance for TransformAddress.
        :type request: :class:`tencentcloud.vpc.v20170312.models.TransformAddressRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.TransformAddressResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("TransformAddress", params, headers=headers)
            response = json.loads(body)
            model = models.TransformAddressResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UnassignIpv6Addresses(self, request):
        """This API is used to release the IPv6 addresses of an ENI. <br />
        This API is completed asynchronously. If you need to query the execution result of an async task, please use the `RequestId` returned by this API to poll the `DescribeVpcTaskResult` API.

        :param request: Request instance for UnassignIpv6Addresses.
        :type request: :class:`tencentcloud.vpc.v20170312.models.UnassignIpv6AddressesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.UnassignIpv6AddressesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UnassignIpv6Addresses", params, headers=headers)
            response = json.loads(body)
            model = models.UnassignIpv6AddressesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UnassignIpv6CidrBlock(self, request):
        """This API (UnassignIpv6CidrBlock) is used to release IPv6 IP ranges.
        If the IP range still has occupied IPs that are not yet repossessed, the IP range cannot be released.

        :param request: Request instance for UnassignIpv6CidrBlock.
        :type request: :class:`tencentcloud.vpc.v20170312.models.UnassignIpv6CidrBlockRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.UnassignIpv6CidrBlockResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UnassignIpv6CidrBlock", params, headers=headers)
            response = json.loads(body)
            model = models.UnassignIpv6CidrBlockResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UnassignIpv6SubnetCidrBlock(self, request):
        """This API (UnassignIpv6SubnetCidrBlock) is used to release IPv6 subnet IP ranges.
        If the subnet IP range still has occupied IPs that are not yet repossessed, the subnet IP range cannot be released.

        :param request: Request instance for UnassignIpv6SubnetCidrBlock.
        :type request: :class:`tencentcloud.vpc.v20170312.models.UnassignIpv6SubnetCidrBlockRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.UnassignIpv6SubnetCidrBlockResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UnassignIpv6SubnetCidrBlock", params, headers=headers)
            response = json.loads(body)
            model = models.UnassignIpv6SubnetCidrBlockResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UnassignPrivateIpAddresses(self, request):
        """This API is used to return the private IP addresses of an ENI.
        * If a secondary private IP of an ENI is returned, the EIP will be automatically unassociated as well. The primary private IP of the ENI cannot be returned.

        This API is completed asynchronously. If you need to query the execution result of an async task, please use the `RequestId` returned by this API to poll the `DescribeVpcTaskResult` API.

        :param request: Request instance for UnassignPrivateIpAddresses.
        :type request: :class:`tencentcloud.vpc.v20170312.models.UnassignPrivateIpAddressesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.UnassignPrivateIpAddressesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UnassignPrivateIpAddresses", params, headers=headers)
            response = json.loads(body)
            model = models.UnassignPrivateIpAddressesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def WithdrawNotifyRoutes(self, request):
        """This API is used to withdraw a route from CCN.

        :param request: Request instance for WithdrawNotifyRoutes.
        :type request: :class:`tencentcloud.vpc.v20170312.models.WithdrawNotifyRoutesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.WithdrawNotifyRoutesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("WithdrawNotifyRoutes", params, headers=headers)
            response = json.loads(body)
            model = models.WithdrawNotifyRoutesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))