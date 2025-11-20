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
from tencentcloud.vpc.v20170312 import models
from typing import Dict


class VpcClient(AbstractClient):
    _apiVersion = '2017-03-12'
    _endpoint = 'vpc.intl.tencentcloudapi.com'
    _service = 'vpc'

    async def AcceptAttachCcnInstances(
            self,
            request: models.AcceptAttachCcnInstancesRequest,
            opts: Dict = None,
    ) -> models.AcceptAttachCcnInstancesResponse:
        """
        This API (AcceptAttachCcnInstances) is used to associate instances across accounts. Cloud Connect Network (CCN) owners accept and agree to the operations.
        """
        
        kwargs = {}
        kwargs["action"] = "AcceptAttachCcnInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AcceptAttachCcnInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AddBandwidthPackageResources(
            self,
            request: models.AddBandwidthPackageResourcesRequest,
            opts: Dict = None,
    ) -> models.AddBandwidthPackageResourcesResponse:
        """
        This API is used to add resources to a bandwidth package, including [Elastic IP](https://intl.cloud.tencent.com/document/product/213/1941?from_cn_redirect=1), [Cloud Load Balancer](https://intl.cloud.tencent.com/document/product/214/517?from_cn_redirect=1), and so on.
        """
        
        kwargs = {}
        kwargs["action"] = "AddBandwidthPackageResources"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddBandwidthPackageResourcesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AddTemplateMember(
            self,
            request: models.AddTemplateMemberRequest,
            opts: Dict = None,
    ) -> models.AddTemplateMemberResponse:
        """
        This API is used to add a parameter template of the IP address, protocol port, IP address group, or protocol port group type.
        """
        
        kwargs = {}
        kwargs["action"] = "AddTemplateMember"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddTemplateMemberResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AdjustPublicAddress(
            self,
            request: models.AdjustPublicAddressRequest,
            opts: Dict = None,
    ) -> models.AdjustPublicAddressResponse:
        """
        This API is used to change the public IP of a CVM or the EIP of the associated bandwidth package.
        """
        
        kwargs = {}
        kwargs["action"] = "AdjustPublicAddress"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AdjustPublicAddressResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AllocateAddresses(
            self,
            request: models.AllocateAddressesRequest,
            opts: Dict = None,
    ) -> models.AllocateAddressesResponse:
        """
        This API is used to apply for one or more [Elastic IP Addresses](https://intl.cloud.tencent.com/document/product/213/1941?from_cn_redirect=1) (EIPs for short).
        * An EIP is a static IP address that is dedicated for dynamic cloud computing. You can quickly re-map an EIP to another instance under your account to protect against instance failures.
        * Your EIP is associated with your Tencent Cloud account rather than an instance. It remains associated with your Tencent Cloud account until you choose to explicitly release it or your account is in arrears for more than 24 hours.
        * The maximum number of EIPs that can be applied for a Tencent Cloud account in each region is restricted. For more information, see [EIP Product Introduction](https://intl.cloud.tencent.com/document/product/213/5733?from_cn_redirect=1). You can get the quota information through the DescribeAddressQuota API.
        """
        
        kwargs = {}
        kwargs["action"] = "AllocateAddresses"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AllocateAddressesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AllocateIPv6Addresses(
            self,
            request: models.AllocateIPv6AddressesRequest,
            opts: Dict = None,
    ) -> models.AllocateIPv6AddressesResponse:
        """
        This API is used to apply for one or more Elastic IPv6 (EIPv6) instances.

        - EIPv6 is a fixed public IPv6 address that can be independently applied for and held in a Tencent Cloud region, providing a consistent product experience with Elastic IPv4.
        - You can quickly bind an EIPv6 instance to the private IPv6 address of a cloud resource, so as to quickly enable IPv6 public bandwidth for the cloud resource.
        - You can also bind an EIPv6 instance to other cloud resources as needed, so as to shield instance failures.
        """
        
        kwargs = {}
        kwargs["action"] = "AllocateIPv6Addresses"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AllocateIPv6AddressesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AllocateIp6AddressesBandwidth(
            self,
            request: models.AllocateIp6AddressesBandwidthRequest,
            opts: Dict = None,
    ) -> models.AllocateIp6AddressesBandwidthResponse:
        """
        This API is used to allocate IPv6 public network bandwidth for classic elastic public IPv6 addresses.

        - Classic elastic public IPv6 addresses only have the private network communication capability by default. They can have the IPv6 public network communication capability and be displayed in the list of Classic Elastic Public IPv6 only after IPv6 public network bandwidth is allocated in the console or by calling this API.
        - You can allocate public network bandwidth for one or multiple Classic elastic public IPv6 addresses each time.
        """
        
        kwargs = {}
        kwargs["action"] = "AllocateIp6AddressesBandwidth"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AllocateIp6AddressesBandwidthResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AssignIpv6Addresses(
            self,
            request: models.AssignIpv6AddressesRequest,
            opts: Dict = None,
    ) -> models.AssignIpv6AddressesResponse:
        """
        This API is used to apply for an IPv6 address for the ENI. <br />
        This API is completed asynchronously. If you need to query the execution result of an async task, please use the `RequestId` returned by this API to poll the `DescribeVpcTaskResult` API.
        * The number of IPs bound with an ENI is limited. For more information, see <a href="/document/product/576/18527">ENI Use Limits</a>.
        * You can apply for a specified IPv6 address. Currently, the IPv6 address can only be used as a secondary IP, instead of the primary IP.
        * The address must be an idle IP in the subnet to which the ENI belongs.
        * When applying for one or more secondary IPv6 addresses for an ENI, the API will return the specified number of secondary IPv6 addresses in the subnet range where the ENI is located.
        """
        
        kwargs = {}
        kwargs["action"] = "AssignIpv6Addresses"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AssignIpv6AddressesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AssignIpv6CidrBlock(
            self,
            request: models.AssignIpv6CidrBlockRequest,
            opts: Dict = None,
    ) -> models.AssignIpv6CidrBlockResponse:
        """
        This API is used to assign IPv6 ranges.
        * To use this API, you must already have a VPC instance. If you do not have a VPC instance yet, use the <a href="https://intl.cloud.tencent.com/document/api/215/15774?from_cn_redirect=1" title="CreateVpc" target="_blank">CreateVpc</a> API to create one.
        * Each VPC can apply for only one IPv6 range.
        """
        
        kwargs = {}
        kwargs["action"] = "AssignIpv6CidrBlock"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AssignIpv6CidrBlockResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AssignIpv6SubnetCidrBlock(
            self,
            request: models.AssignIpv6SubnetCidrBlockRequest,
            opts: Dict = None,
    ) -> models.AssignIpv6SubnetCidrBlockResponse:
        """
        This API (AssignIpv6SubnetCidrBlock) is used to assign IPv6 subnet IP ranges.
        * To assign an `IPv6` IP range to a subnet, the `VPC` that the subnet belongs to should have obtained the `IPv6` IP range. If this has not been assigned, use the `AssignIpv6CidrBlock` API to assign an `IPv6` IP range to the `VPC` to which the subnet belongs. Otherwise, the `IPv6` subnet IP range cannot be assigned.
        * Each subnet can only be assigned one IPv6 IP range.
        """
        
        kwargs = {}
        kwargs["action"] = "AssignIpv6SubnetCidrBlock"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AssignIpv6SubnetCidrBlockResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AssignPrivateIpAddresses(
            self,
            request: models.AssignPrivateIpAddressesRequest,
            opts: Dict = None,
    ) -> models.AssignPrivateIpAddressesResponse:
        """
        This API is used to apply for private IPs for an ENI.
        * An ENI can only be bound with a limited number of IP addresses. For more information about resource limits, see <a href="/document/product/576/18527">ENI Use Limits</a>.
        * You can apply for a specified private IP. It cannot be a primary IP because the primary IP already exists and cannot be modified. The private IP address must be an idle IP in the subnet to which the ENI belongs.
        * You can apply for more than one secondary private IP on the ENI. The API will return the specified number of secondary private IPs in the subnet IP range.
        >?This API is async. You can call the [`DescribeVpcTaskResult`](https://intl.cloud.tencent.com/document/api/215/59037?from_cn_redirect=1) API to query the task result. When the task is completed, you can continue other tasks.
        >
        """
        
        kwargs = {}
        kwargs["action"] = "AssignPrivateIpAddresses"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AssignPrivateIpAddressesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AssociateAddress(
            self,
            request: models.AssociateAddressRequest,
            opts: Dict = None,
    ) -> models.AssociateAddressResponse:
        """
        This API is used to bind an [Elastic IP](https://intl.cloud.tencent.com/document/product/213/1941?from_cn_redirect=1) (EIP for short) to the specified private IP of an instance or ENI.
        * Binding an EIP to a CVM instance is actually binding the EIP to the primary private IP of the primary ENI on the CVM instance.
        * When an EIP is bound, the public IP previously bound to the CVM instance will be unbound and released automatically.
        * To bind another EIP to the private IP of the specified ENI, you must first unbind the EIP.
        * To bind an EIP to a NAT Gateway, use the API [AssociateNatGatewayAddress](https://intl.cloud.tencent.com/document/product/215/36722?from_cn_redirect=1).
        * An EIP cannot be bound if it’s overdue or blocked
        * Only EIP in the `UNBIND` status can be bound.
        """
        
        kwargs = {}
        kwargs["action"] = "AssociateAddress"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AssociateAddressResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AssociateDirectConnectGatewayNatGateway(
            self,
            request: models.AssociateDirectConnectGatewayNatGatewayRequest,
            opts: Dict = None,
    ) -> models.AssociateDirectConnectGatewayNatGatewayResponse:
        """
        This API is used to bind a direct connect gateway with a NAT gateway,  and direct its default route to the NAT Gateway.
        """
        
        kwargs = {}
        kwargs["action"] = "AssociateDirectConnectGatewayNatGateway"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AssociateDirectConnectGatewayNatGatewayResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AssociateIPv6Address(
            self,
            request: models.AssociateIPv6AddressRequest,
            opts: Dict = None,
    ) -> models.AssociateIPv6AddressResponse:
        """
        This API is used to bind an EIPv6 instance to the private IPv6 address configured on the CVM or ENI.

        - Binding an EIPv6 to the CVM essentially indicates binding the EIPv6 to the private IPv6 address configured on the ENI of the CVM.
        - Before binding an EIPv6 to the private IPv6 of a specified ENI, ensure that the private IPv6 address is unbound before the binding operation is performed.
        """
        
        kwargs = {}
        kwargs["action"] = "AssociateIPv6Address"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AssociateIPv6AddressResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AssociateNatGatewayAddress(
            self,
            request: models.AssociateNatGatewayAddressRequest,
            opts: Dict = None,
    ) -> models.AssociateNatGatewayAddressResponse:
        """
        This API is used to bind an EIP to a NAT gateway.
        """
        
        kwargs = {}
        kwargs["action"] = "AssociateNatGatewayAddress"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AssociateNatGatewayAddressResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AssociateNetworkAclSubnets(
            self,
            request: models.AssociateNetworkAclSubnetsRequest,
            opts: Dict = None,
    ) -> models.AssociateNetworkAclSubnetsResponse:
        """
        This API is used to associate a network ACL with subnets in a VPC instance.
        """
        
        kwargs = {}
        kwargs["action"] = "AssociateNetworkAclSubnets"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AssociateNetworkAclSubnetsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AssociateNetworkInterfaceSecurityGroups(
            self,
            request: models.AssociateNetworkInterfaceSecurityGroupsRequest,
            opts: Dict = None,
    ) -> models.AssociateNetworkInterfaceSecurityGroupsResponse:
        """
        This API (AssociateNetworkInterfaceSecurityGroups) is used to attach a security group to an ENI.
        """
        
        kwargs = {}
        kwargs["action"] = "AssociateNetworkInterfaceSecurityGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AssociateNetworkInterfaceSecurityGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AttachCcnInstances(
            self,
            request: models.AttachCcnInstancesRequest,
            opts: Dict = None,
    ) -> models.AttachCcnInstancesResponse:
        """
        This API is used to add a network instance to a CCN instance. Network instances include VPCs and Direct Connect gateways. <br />
        The number of network instances that each CCN can be associated with is limited. For more information, see the product documentation. If you need to associate more instances, please submit a ticket.
        """
        
        kwargs = {}
        kwargs["action"] = "AttachCcnInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AttachCcnInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AttachClassicLinkVpc(
            self,
            request: models.AttachClassicLinkVpcRequest,
            opts: Dict = None,
    ) -> models.AttachClassicLinkVpcResponse:
        """
        This API is used to create a Classiclink between a VPC instance and a classic network device.
        * The VPC instance and the classic network device must be in the same region.
        * For differences between VPC and the classic network, see <a href="https://intl.cloud.tencent.com/document/product/215/30720?from_cn_redirect=1">VPC and Classic Network</a>.
        >?This API is async. You can call the [`DescribeVpcTaskResult`](https://intl.cloud.tencent.com/document/api/215/59037?from_cn_redirect=1) API to query the task result. When the task is completed, you can continue other tasks.
        >
        """
        
        kwargs = {}
        kwargs["action"] = "AttachClassicLinkVpc"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AttachClassicLinkVpcResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AttachNetworkInterface(
            self,
            request: models.AttachNetworkInterfaceRequest,
            opts: Dict = None,
    ) -> models.AttachNetworkInterfaceResponse:
        """
        This API is used to bind an ENI to a CVM.
        * An ENI must be bound with one security group at least. To bind it, see <a href="https://intl.cloud.tencent.com/document/product/215/43132?from_cn_redirect=1">AssociateNetworkInterfaceSecurityGroups</a>.
        * One CVM can be bound with multiple ENIs, but only one can be the primary ENI. For more information about the limits, see <a href="https://intl.cloud.tencent.com/document/product/576/18527?from_cn_redirect=1">ENI Use Limits</a>.
        * An ENI can only be bound to one CVM.
        * Only the running or shutdown CVMs can be bound with ENIs. For more information about the CVM status, see <a href="https://intl.cloud.tencent.com/document/api/213/9452?from_cn_redirect=1#InstanceStatus">InstanceStatus</a> in the Data Types.
        * An ENI can only be bound to a VPC-based CVM under the same availability zone as the ENI subnet.

        This API is completed asynchronously. If you need to query the execution result of an async task, please use the `RequestId` returned by this API to poll the `DescribeVpcTaskResult` API.
        """
        
        kwargs = {}
        kwargs["action"] = "AttachNetworkInterface"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AttachNetworkInterfaceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AttachSnapshotInstances(
            self,
            request: models.AttachSnapshotInstancesRequest,
            opts: Dict = None,
    ) -> models.AttachSnapshotInstancesResponse:
        """
        This API is used to associate a snapshot policy with specified instances.
        """
        
        kwargs = {}
        kwargs["action"] = "AttachSnapshotInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AttachSnapshotInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AuditCrossBorderCompliance(
            self,
            request: models.AuditCrossBorderComplianceRequest,
            opts: Dict = None,
    ) -> models.AuditCrossBorderComplianceResponse:
        """
        This API is used by the service provider to perform a compliance audit.
        * This API is only provided for service providers to audit compliance review requests received. Tencent Cloud will verify the identity of the service provider by the `APPID`.
        * The status of the review request can be changed between `APPROVED` and `DENY`.
        """
        
        kwargs = {}
        kwargs["action"] = "AuditCrossBorderCompliance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AuditCrossBorderComplianceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CheckAssistantCidr(
            self,
            request: models.CheckAssistantCidrRequest,
            opts: Dict = None,
    ) -> models.CheckAssistantCidrResponse:
        """
        This API is used to check whether the secondary CIDR block conflicts with existing routes, peering connections (peer VPC CIDR blocks), and other resources.
        * Check whether the secondary CIDR block overlaps with the primary/secondary CIDR block of the current VPC.
        * Check whether the secondary CIDR block overlaps with the routing destination of the current VPC.
        * If the current VPC is used in a peering connection, check whether the secondary CIDR block overlaps with the primary/secondary CIDR block of the peer VPC.
        """
        
        kwargs = {}
        kwargs["action"] = "CheckAssistantCidr"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CheckAssistantCidrResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CheckNetDetectState(
            self,
            request: models.CheckNetDetectStateRequest,
            opts: Dict = None,
    ) -> models.CheckNetDetectStateResponse:
        """
        This API is used to verify the network detection status.
        """
        
        kwargs = {}
        kwargs["action"] = "CheckNetDetectState"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CheckNetDetectStateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CloneSecurityGroup(
            self,
            request: models.CloneSecurityGroupRequest,
            opts: Dict = None,
    ) -> models.CloneSecurityGroupResponse:
        """
        This API is used to create a security group with the same rule configurations as an existing security group. The cloning only copies the security group and its rules, but not the security group tags.
        """
        
        kwargs = {}
        kwargs["action"] = "CloneSecurityGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CloneSecurityGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAddressTemplate(
            self,
            request: models.CreateAddressTemplateRequest,
            opts: Dict = None,
    ) -> models.CreateAddressTemplateResponse:
        """
        This API is used to create an IP address template.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAddressTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAddressTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAddressTemplateGroup(
            self,
            request: models.CreateAddressTemplateGroupRequest,
            opts: Dict = None,
    ) -> models.CreateAddressTemplateGroupResponse:
        """
        This API is used to create an IP address template group.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAddressTemplateGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAddressTemplateGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAndAttachNetworkInterface(
            self,
            request: models.CreateAndAttachNetworkInterfaceRequest,
            opts: Dict = None,
    ) -> models.CreateAndAttachNetworkInterfaceResponse:
        """
        This API is used to create an ENI and bind it to a CVM.
        * You can specify private IP addresses and a primary IP when creating an ENI. The specified private IP must be idle and in the same subnet as the ENI.
        * When creating an ENI, you can specify the number of private IPs that you want to apply for. The system will randomly generate private IP addresses.
        * The number of IPs bound with an ENI is limited. For more information, see <a href="/document/product/576/18527">ENI Use Limits</a>.
        * You can bind an existing security group when creating an ENI.
        * You can bind a tag when creating an ENI. The tag list in the response indicates the tags that have been successfully added.
        >?This API is async. You can call the [`DescribeVpcTaskResult`](https://intl.cloud.tencent.com/document/api/215/59037?from_cn_redirect=1) API to query the task result. When the task is completed, you can continue other tasks.
        >
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAndAttachNetworkInterface"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAndAttachNetworkInterfaceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAssistantCidr(
            self,
            request: models.CreateAssistantCidrRequest,
            opts: Dict = None,
    ) -> models.CreateAssistantCidrResponse:
        """
        This API is used to batch create secondary CIDR blocks.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAssistantCidr"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAssistantCidrResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateBandwidthPackage(
            self,
            request: models.CreateBandwidthPackageRequest,
            opts: Dict = None,
    ) -> models.CreateBandwidthPackageResponse:
        """
        This API is used to create a [device bandwidth package](https://intl.cloud.tencent.com/document/product/684/15245?from_cn_redirect=1#bwptype) or an [IP bandwidth package](https://intl.cloud.tencent.com/document/product/684/15245?from_cn_redirect=1#bwptype).
        """
        
        kwargs = {}
        kwargs["action"] = "CreateBandwidthPackage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateBandwidthPackageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCcn(
            self,
            request: models.CreateCcnRequest,
            opts: Dict = None,
    ) -> models.CreateCcnResponse:
        """
        This API is used to create a CCN instance.
        * You can add tags to a CCN instance upon the creation. The tags are added successfully if they are listed in the response.
        * There is a quota of CCN instances for each account. For more information, see product documentation. To increase the quota, please submit a ticket.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCcn"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCcnResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCustomerGateway(
            self,
            request: models.CreateCustomerGatewayRequest,
            opts: Dict = None,
    ) -> models.CreateCustomerGatewayResponse:
        """
        This API (CreateCustomerGateway) is used to create customer gateways.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCustomerGateway"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCustomerGatewayResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDefaultVpc(
            self,
            request: models.CreateDefaultVpcRequest,
            opts: Dict = None,
    ) -> models.CreateDefaultVpcResponse:
        """
        This API is used to create a VPC with default settings.

        To create a VPC with custom settings, such as VPC name, IP range, subnet IP range, and subnet availability zone, use `CreateVpc` instead.

        This API may not create a default VPC. It depends on the network attributes (`DescribeAccountAttributes`) of your account.
        * If both basic network and VPC are supported, the returned `VpcId` is 0.
        * If only VPC is supported, the default VPC information is returned.

        You can also use the `Force` parameter to forcibly return a default VPC.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDefaultVpc"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDefaultVpcResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDirectConnectGateway(
            self,
            request: models.CreateDirectConnectGatewayRequest,
            opts: Dict = None,
    ) -> models.CreateDirectConnectGatewayResponse:
        """
        This API is used to create a direct connect gateway.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDirectConnectGateway"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDirectConnectGatewayResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDirectConnectGatewayCcnRoutes(
            self,
            request: models.CreateDirectConnectGatewayCcnRoutesRequest,
            opts: Dict = None,
    ) -> models.CreateDirectConnectGatewayCcnRoutesResponse:
        """
        This API (CreateDirectConnectGatewayCcnRoutes) is used to create the CCN route (IDC IP range) of a Direct Connect gateway.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDirectConnectGatewayCcnRoutes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDirectConnectGatewayCcnRoutesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateFlowLog(
            self,
            request: models.CreateFlowLogRequest,
            opts: Dict = None,
    ) -> models.CreateFlowLogResponse:
        """
        This API is used to create a flow log.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateFlowLog"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateFlowLogResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateHaVip(
            self,
            request: models.CreateHaVipRequest,
            opts: Dict = None,
    ) -> models.CreateHaVipResponse:
        """
        This API is used to create a highly available virtual IP (HAVIP).
        """
        
        kwargs = {}
        kwargs["action"] = "CreateHaVip"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateHaVipResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateLocalGateway(
            self,
            request: models.CreateLocalGatewayRequest,
            opts: Dict = None,
    ) -> models.CreateLocalGatewayResponse:
        """
        This API is used to create a local gateway for a CDC instance.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateLocalGateway"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateLocalGatewayResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateNatGateway(
            self,
            request: models.CreateNatGatewayRequest,
            opts: Dict = None,
    ) -> models.CreateNatGatewayResponse:
        """
        This API is used to create a NAT Gateway.
        Before taking actions on a NAT gateway, ensure that it has been successfully created, namely, the `State` field in the response of the `DescribeNatGateway` API is `AVAILABLE`.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateNatGateway"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateNatGatewayResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateNatGatewayDestinationIpPortTranslationNatRule(
            self,
            request: models.CreateNatGatewayDestinationIpPortTranslationNatRuleRequest,
            opts: Dict = None,
    ) -> models.CreateNatGatewayDestinationIpPortTranslationNatRuleResponse:
        """
        This API is used to create the port forwarding rules of a NAT gateway.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateNatGatewayDestinationIpPortTranslationNatRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateNatGatewayDestinationIpPortTranslationNatRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateNatGatewaySourceIpTranslationNatRule(
            self,
            request: models.CreateNatGatewaySourceIpTranslationNatRuleRequest,
            opts: Dict = None,
    ) -> models.CreateNatGatewaySourceIpTranslationNatRuleResponse:
        """
        This API is used to create SNAT rules for a NAT gateway.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateNatGatewaySourceIpTranslationNatRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateNatGatewaySourceIpTranslationNatRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateNetDetect(
            self,
            request: models.CreateNetDetectRequest,
            opts: Dict = None,
    ) -> models.CreateNetDetectResponse:
        """
        This API is used to create a network probe.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateNetDetect"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateNetDetectResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateNetworkAcl(
            self,
            request: models.CreateNetworkAclRequest,
            opts: Dict = None,
    ) -> models.CreateNetworkAclResponse:
        """
        This API is used to create a <a href="https://intl.cloud.tencent.com/document/product/215/20088?from_cn_redirect=1">network ACL</a>.
        * The inbound and outbound rules for a new network ACL are "Deny All" by default. You need to call `ModifyNetworkAclEntries` to set rules for the new network ACL as needed.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateNetworkAcl"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateNetworkAclResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateNetworkAclQuintupleEntries(
            self,
            request: models.CreateNetworkAclQuintupleEntriesRequest,
            opts: Dict = None,
    ) -> models.CreateNetworkAclQuintupleEntriesResponse:
        """
        This API is used to add one or more in/outbound rules of the network ACL quintuple.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateNetworkAclQuintupleEntries"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateNetworkAclQuintupleEntriesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateNetworkInterface(
            self,
            request: models.CreateNetworkInterfaceRequest,
            opts: Dict = None,
    ) -> models.CreateNetworkInterfaceResponse:
        """
        This API is used to create an ENI.
        * You can specify private IP addresses and a primary IP when creating an ENI. The specified private IP must be in the same subnet as the ENI and is not occupied.
        * When creating an ENI, you can specify the number of private IP addresses that you want to apply for. The system will randomly generate private IP addresses.
        * An ENI can only be bound with a limited number of IP addresses. For more information about resource limits, see <a href="/document/product/576/18527">ENI Use Limits</a>.
        * You can bind an existing security group when creating an ENI.
        * You can bind a tag when creating an ENI. The tag list in the response indicates the tags that have been successfully added.
        >?This API is async. You can call the [`DescribeVpcTaskResult`](https://intl.cloud.tencent.com/document/api/215/59037?from_cn_redirect=1) API to query the task result. When the task is completed, you can continue other tasks.
        >
        """
        
        kwargs = {}
        kwargs["action"] = "CreateNetworkInterface"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateNetworkInterfaceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateReserveIpAddresses(
            self,
            request: models.CreateReserveIpAddressesRequest,
            opts: Dict = None,
    ) -> models.CreateReserveIpAddressesResponse:
        """
        This API is used to create a reserved private IP address.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateReserveIpAddresses"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateReserveIpAddressesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateRoutePolicy(
            self,
            request: models.CreateRoutePolicyRequest,
            opts: Dict = None,
    ) -> models.CreateRoutePolicyResponse:
        """
        This API is used to create a VPC route reception policy, including name, description and policy entries.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateRoutePolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateRoutePolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateRoutePolicyAssociations(
            self,
            request: models.CreateRoutePolicyAssociationsRequest,
            opts: Dict = None,
    ) -> models.CreateRoutePolicyAssociationsResponse:
        """
        This API is used to create route reception policy bindings (the binding relationship between policy instances and route table instances as well as set priorities).
        """
        
        kwargs = {}
        kwargs["action"] = "CreateRoutePolicyAssociations"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateRoutePolicyAssociationsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateRoutePolicyEntries(
            self,
            request: models.CreateRoutePolicyEntriesRequest,
            opts: Dict = None,
    ) -> models.CreateRoutePolicyEntriesResponse:
        """
        This API is used to create route reception policy entries.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateRoutePolicyEntries"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateRoutePolicyEntriesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateRouteTable(
            self,
            request: models.CreateRouteTableRequest,
            opts: Dict = None,
    ) -> models.CreateRouteTableResponse:
        """
        This API is used to create a route table.
        * After the VPC instance has been created, the system creates a default route table with which all newly created subnets will be associated. By default, you can use this route table to manage your routing policies. If you have multiple routing policies, you can call the API for creating route tables to create more route tables to manage these routing policies.
        * You can bind a tag when creating a route table. The tag list in the response indicates the tags that have been successfully added.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateRouteTable"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateRouteTableResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateRoutes(
            self,
            request: models.CreateRoutesRequest,
            opts: Dict = None,
    ) -> models.CreateRoutesResponse:
        """
        This API is used to create routes.
        * You can batch add routes to a specified route table.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateRoutes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateRoutesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateSecurityGroup(
            self,
            request: models.CreateSecurityGroupRequest,
            opts: Dict = None,
    ) -> models.CreateSecurityGroupResponse:
        """
        This API is used to create a security group (SecurityGroup).
        * Note the <a href="https://intl.cloud.tencent.com/document/product/213/12453?from_cn_redirect=1">maximum number of security groups</a> per project in each region under each account.
        * Both the inbound and outbound rules for a newly created security group are "Deny All" by default. You need to call CreateSecurityGroupPolicies to set security group rules based on your needs.
        * You can bind a tag when creating a security group. The tag list in the response indicates the tags that have been successfully added.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateSecurityGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateSecurityGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateSecurityGroupPolicies(
            self,
            request: models.CreateSecurityGroupPoliciesRequest,
            opts: Dict = None,
    ) -> models.CreateSecurityGroupPoliciesResponse:
        """
        This API is used to create security group policies (`SecurityGroupPolicy`).

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
        """
        
        kwargs = {}
        kwargs["action"] = "CreateSecurityGroupPolicies"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateSecurityGroupPoliciesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateSecurityGroupWithPolicies(
            self,
            request: models.CreateSecurityGroupWithPoliciesRequest,
            opts: Dict = None,
    ) -> models.CreateSecurityGroupWithPoliciesResponse:
        """
        This API is used to create a security group, and add security group policies.
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
        """
        
        kwargs = {}
        kwargs["action"] = "CreateSecurityGroupWithPolicies"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateSecurityGroupWithPoliciesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateServiceTemplate(
            self,
            request: models.CreateServiceTemplateRequest,
            opts: Dict = None,
    ) -> models.CreateServiceTemplateResponse:
        """
        This API (CreateServiceTemplate) is used to create a protocol port template.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateServiceTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateServiceTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateServiceTemplateGroup(
            self,
            request: models.CreateServiceTemplateGroupRequest,
            opts: Dict = None,
    ) -> models.CreateServiceTemplateGroupResponse:
        """
        This API (CreateServiceTemplateGroup) is used to create a protocol port template group.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateServiceTemplateGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateServiceTemplateGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateSnapshotPolicies(
            self,
            request: models.CreateSnapshotPoliciesRequest,
            opts: Dict = None,
    ) -> models.CreateSnapshotPoliciesResponse:
        """
        This API is used to create snapshot policies.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateSnapshotPolicies"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateSnapshotPoliciesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateSubnet(
            self,
            request: models.CreateSubnetRequest,
            opts: Dict = None,
    ) -> models.CreateSubnetResponse:
        """
        This API is used to create a subnet.
        * You must create a VPC instance before creating a subnet.
        * After the subnet is successfully created, its IP address range cannot be modified. The subnet IP address range must fall within the VPC IP address range. They can be the same if the VPC instance has only one subnet. We recommend that you keep the subnet IP address range within the VPC IP address range to reserve IP address ranges for other subnets.
        * The subnet mask of the smallest IP address range that can be created is 28 (16 IP addresses), and that of the largest IP address range is 16 (65,536 IP addresses).
        * IP address ranges of different subnets cannot overlap with each other within the same VPC instance.
        * A subnet is automatically associated with the default route table once created.
        * You can bind a tag when creating a subnet. The tag list in the response indicates the tags that have been successfully added.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateSubnet"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateSubnetResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateSubnets(
            self,
            request: models.CreateSubnetsRequest,
            opts: Dict = None,
    ) -> models.CreateSubnetsResponse:
        """
        This API is used to create subnets in batches.
        * You must create a VPC instance before creating a subnet.
        * After the subnet is successfully created, its IP address range cannot be modified. The subnet IP address range must fall within the VPC IP address range. They can be the same if the VPC has only one subnet. We recommend that you keep the subnet IP address range within the VPC IP address range to reserve IP address ranges for other subnets.
        * The subnet mask of the smallest IP address range that can be created is 28 (16 IP addresses), and that of the largest IP address range is 16 (65,536 IP addresses).
        * IP address ranges of different subnets cannot overlap with each other within the same VPC instance.
        * A subnet is automatically associated with the default route table once created.
        * You can bind a tag when creating a subnet. The tag list in the response indicates the tags that have been successfully added.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateSubnets"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateSubnetsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateVpc(
            self,
            request: models.CreateVpcRequest,
            opts: Dict = None,
    ) -> models.CreateVpcResponse:
        """
        This API is used to create a VPC instance.
        * The subnet mask of the smallest IP address range that can be created is 28 (16 IP addresses), that of the largest IP address ranges 10.0.0.0/12 and 172.16.0.0/12 is 12 (1,048,576 IP addresses), and that of the largest IP address range 192.168.0.0/16 is 16 (65,536 IP addresses). For more information on how to plan VPC IP ranges, see [Network Planning](https://intl.cloud.tencent.com/document/product/215/30313?from_cn_redirect=1).
        * The number of VPC instances that can be created in a region is limited. For more information, see <a href="https://intl.cloud.tencent.com/doc/product/215/537?from_cn_redirect=1" title="VPC Use Limits">VPC Use Limits</a>. To request more resources, [submit a ticket](https://console.cloud.tencent.com/workorder/category).
        * You can bind tags when creating a VPC instance. The tag list in the response indicates the tags that have been successfully added.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateVpc"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateVpcResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateVpcEndPoint(
            self,
            request: models.CreateVpcEndPointRequest,
            opts: Dict = None,
    ) -> models.CreateVpcEndPointResponse:
        """
        This API is used to create an endpoint.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateVpcEndPoint"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateVpcEndPointResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateVpcEndPointService(
            self,
            request: models.CreateVpcEndPointServiceRequest,
            opts: Dict = None,
    ) -> models.CreateVpcEndPointServiceResponse:
        """
        This API is used to create an endpoint service.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateVpcEndPointService"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateVpcEndPointServiceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateVpcEndPointServiceWhiteList(
            self,
            request: models.CreateVpcEndPointServiceWhiteListRequest,
            opts: Dict = None,
    ) -> models.CreateVpcEndPointServiceWhiteListResponse:
        """
        This API is used to create the endpoint service allowlist.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateVpcEndPointServiceWhiteList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateVpcEndPointServiceWhiteListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateVpnConnection(
            self,
            request: models.CreateVpnConnectionRequest,
            opts: Dict = None,
    ) -> models.CreateVpnConnectionResponse:
        """
        This API is used to create a VPN tunnel.
        >?This API is async. You can call the [`DescribeVpcTaskResult`](https://intl.cloud.tencent.com/document/api/215/59037?from_cn_redirect=1) API to query the task result. When the task is completed, you can continue other tasks.
        >
        """
        
        kwargs = {}
        kwargs["action"] = "CreateVpnConnection"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateVpnConnectionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateVpnGateway(
            self,
            request: models.CreateVpnGatewayRequest,
            opts: Dict = None,
    ) -> models.CreateVpnGatewayResponse:
        """
        This API (CreateVpnGateway) is used to create a VPN gateway.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateVpnGateway"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateVpnGatewayResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateVpnGatewayRoutes(
            self,
            request: models.CreateVpnGatewayRoutesRequest,
            opts: Dict = None,
    ) -> models.CreateVpnGatewayRoutesResponse:
        """
        This API is used to create destination routes of a route-based VPN gateway.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateVpnGatewayRoutes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateVpnGatewayRoutesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteAddressTemplate(
            self,
            request: models.DeleteAddressTemplateRequest,
            opts: Dict = None,
    ) -> models.DeleteAddressTemplateResponse:
        """
        This API (DeleteAddressTemplate) is used to delete an IP address template.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAddressTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAddressTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteAddressTemplateGroup(
            self,
            request: models.DeleteAddressTemplateGroupRequest,
            opts: Dict = None,
    ) -> models.DeleteAddressTemplateGroupResponse:
        """
        This API (DeleteAddressTemplateGroup) is used to delete an IP address template group.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAddressTemplateGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAddressTemplateGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteAssistantCidr(
            self,
            request: models.DeleteAssistantCidrRequest,
            opts: Dict = None,
    ) -> models.DeleteAssistantCidrResponse:
        """
        This API is used to delete a secondary CIDR block.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAssistantCidr"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAssistantCidrResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteBandwidthPackage(
            self,
            request: models.DeleteBandwidthPackageRequest,
            opts: Dict = None,
    ) -> models.DeleteBandwidthPackageResponse:
        """
        This API is used to delete bandwidth packages, including [device bandwidth packages](https://intl.cloud.tencent.com/document/product/684/15246?from_cn_redirect=1#.E8.AE.BE.E5.A4.87.E5.B8.A6.E5.AE.BD.E5.8C.85) and [IP bandwidth packages](https://intl.cloud.tencent.com/document/product/684/15246?from_cn_redirect=1#ip-.E5.B8.A6.E5.AE.BD.E5.8C.85).
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteBandwidthPackage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteBandwidthPackageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteCcn(
            self,
            request: models.DeleteCcnRequest,
            opts: Dict = None,
    ) -> models.DeleteCcnResponse:
        """
        This API (DeleteCcn) is used to delete CCNs.
        * After deletion, the routes between all instances associated with the CCN will be deleted, and the network will be interrupted. Please confirm this operation in advance.
        * CCN deletion is an irreversible operation. Please proceed with caution.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteCcn"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteCcnResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteCustomerGateway(
            self,
            request: models.DeleteCustomerGatewayRequest,
            opts: Dict = None,
    ) -> models.DeleteCustomerGatewayResponse:
        """
        This API (DeleteCustomerGateway) is used to delete customer gateways.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteCustomerGateway"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteCustomerGatewayResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteDirectConnectGateway(
            self,
            request: models.DeleteDirectConnectGatewayRequest,
            opts: Dict = None,
    ) -> models.DeleteDirectConnectGatewayResponse:
        """
        This API is used to delete a direct connect gateway.
        <li>For a NAT gateway, NAT and ACL rules will be cleared upon the deletion of a direct connect gateway.
        <li>After the deletion of a direct connect gateway, the routing policy associated with the gateway in the route table will also be deleted.
        This API is completed asynchronously. If you need to query the async job execution results, please use the `RequestId` returned by this API to poll the `QueryTask` API.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteDirectConnectGateway"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteDirectConnectGatewayResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteDirectConnectGatewayCcnRoutes(
            self,
            request: models.DeleteDirectConnectGatewayCcnRoutesRequest,
            opts: Dict = None,
    ) -> models.DeleteDirectConnectGatewayCcnRoutesResponse:
        """
        This API (DeleteDirectConnectGatewayCcnRoutes) is used to delete the CCN routes (IDC IP range) of a Direct Connect gateway.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteDirectConnectGatewayCcnRoutes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteDirectConnectGatewayCcnRoutesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteFlowLog(
            self,
            request: models.DeleteFlowLogRequest,
            opts: Dict = None,
    ) -> models.DeleteFlowLogResponse:
        """
        This API is used to delete a flow log.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteFlowLog"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteFlowLogResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteHaVip(
            self,
            request: models.DeleteHaVipRequest,
            opts: Dict = None,
    ) -> models.DeleteHaVipResponse:
        """
        This API is used to delete an HAVIP. <br />
        This API is completed asynchronously. If you need to query the execution result of an async task, please use the `RequestId` returned by this API to poll the `DescribeVpcTaskResult` API.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteHaVip"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteHaVipResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteLocalGateway(
            self,
            request: models.DeleteLocalGatewayRequest,
            opts: Dict = None,
    ) -> models.DeleteLocalGatewayResponse:
        """
        This API is used to delete the local gateway of a CDC instance.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteLocalGateway"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteLocalGatewayResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteNatGateway(
            self,
            request: models.DeleteNatGatewayRequest,
            opts: Dict = None,
    ) -> models.DeleteNatGatewayResponse:
        """
        This API is used to delete a NAT gateway.
        When a NAT gateway is deleted, all routes containing this gateway are deleted automatically, and the elastic IP is unbound.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteNatGateway"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteNatGatewayResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteNatGatewayDestinationIpPortTranslationNatRule(
            self,
            request: models.DeleteNatGatewayDestinationIpPortTranslationNatRuleRequest,
            opts: Dict = None,
    ) -> models.DeleteNatGatewayDestinationIpPortTranslationNatRuleResponse:
        """
        This API is used to delete the port forwarding rule of a NAT gateway.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteNatGatewayDestinationIpPortTranslationNatRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteNatGatewayDestinationIpPortTranslationNatRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteNatGatewaySourceIpTranslationNatRule(
            self,
            request: models.DeleteNatGatewaySourceIpTranslationNatRuleRequest,
            opts: Dict = None,
    ) -> models.DeleteNatGatewaySourceIpTranslationNatRuleResponse:
        """
        This API is used to delete a SNAT forwarding rule of a NAT gateway.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteNatGatewaySourceIpTranslationNatRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteNatGatewaySourceIpTranslationNatRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteNetDetect(
            self,
            request: models.DeleteNetDetectRequest,
            opts: Dict = None,
    ) -> models.DeleteNetDetectResponse:
        """
        This API is used to delete a network probe.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteNetDetect"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteNetDetectResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteNetworkAcl(
            self,
            request: models.DeleteNetworkAclRequest,
            opts: Dict = None,
    ) -> models.DeleteNetworkAclResponse:
        """
        This API is used to delete a network ACL.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteNetworkAcl"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteNetworkAclResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteNetworkAclQuintupleEntries(
            self,
            request: models.DeleteNetworkAclQuintupleEntriesRequest,
            opts: Dict = None,
    ) -> models.DeleteNetworkAclQuintupleEntriesResponse:
        """
        This API is used to delete specified in/outbound rules of the network ACL quintuple. In the `NetworkAclQuintupleEntrySet` parameters, `NetworkAclQuintupleEntryId` is required for `NetworkAclQuintupleEntry`.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteNetworkAclQuintupleEntries"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteNetworkAclQuintupleEntriesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteNetworkInterface(
            self,
            request: models.DeleteNetworkInterfaceRequest,
            opts: Dict = None,
    ) -> models.DeleteNetworkInterfaceResponse:
        """
        This API is used to delete an ENI.
        * An ENI cannot be deleted when it’s bound to a CVM.
         * After the deletion, all of its private IP addresses will be released.

        This API is completed asynchronously. If you need to query the execution result of an async task, please use the `RequestId` returned by this API to poll the `DescribeVpcTaskResult` API.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteNetworkInterface"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteNetworkInterfaceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteReserveIpAddresses(
            self,
            request: models.DeleteReserveIpAddressesRequest,
            opts: Dict = None,
    ) -> models.DeleteReserveIpAddressesResponse:
        """
        This API is used to delete a reserved private IP address.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteReserveIpAddresses"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteReserveIpAddressesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteRoutePolicy(
            self,
            request: models.DeleteRoutePolicyRequest,
            opts: Dict = None,
    ) -> models.DeleteRoutePolicyResponse:
        """
        This API is used to delete a route reception policy and entries.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteRoutePolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteRoutePolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteRoutePolicyAssociations(
            self,
            request: models.DeleteRoutePolicyAssociationsRequest,
            opts: Dict = None,
    ) -> models.DeleteRoutePolicyAssociationsResponse:
        """
        This API is used to delete route reception policy bindings (the binding relationship between route reception policy objects and route tables).
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteRoutePolicyAssociations"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteRoutePolicyAssociationsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteRoutePolicyEntries(
            self,
            request: models.DeleteRoutePolicyEntriesRequest,
            opts: Dict = None,
    ) -> models.DeleteRoutePolicyEntriesResponse:
        """
        This API is used to delete route reception policy entries.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteRoutePolicyEntries"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteRoutePolicyEntriesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteRouteTable(
            self,
            request: models.DeleteRouteTableRequest,
            opts: Dict = None,
    ) -> models.DeleteRouteTableResponse:
        """
        This API is used to delete a route table.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteRouteTable"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteRouteTableResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteRoutes(
            self,
            request: models.DeleteRoutesRequest,
            opts: Dict = None,
    ) -> models.DeleteRoutesResponse:
        """
        This API (DeleteRoutes) is used to delete routing policies in batches from a route table.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteRoutes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteRoutesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteSecurityGroup(
            self,
            request: models.DeleteSecurityGroupRequest,
            opts: Dict = None,
    ) -> models.DeleteSecurityGroupResponse:
        """
        This API (DeleteSecurityGroup) is used to delete security groups (SecurityGroup).
        * Only security groups under the current account can be deleted.
        * A security group cannot be deleted directly if its instance ID is used in the policy of another security group. You need to modify the policy first and then delete the security group.
        * A security group cannot be recovered after deletion, please proceed with caution.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteSecurityGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteSecurityGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteSecurityGroupPolicies(
            self,
            request: models.DeleteSecurityGroupPoliciesRequest,
            opts: Dict = None,
    ) -> models.DeleteSecurityGroupPoliciesResponse:
        """
        This API (DeleteSecurityGroupPolicies) is used to delete security group policies (SecurityGroupPolicy).
        * SecurityGroupPolicySet.Version is used to specify the version of the security group you are operating. If the specified Version number differs from the latest version of the current security group, a failure will be returned. If Version is not specified, the policy of the specified PolicyIndex will be deleted directly.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteSecurityGroupPolicies"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteSecurityGroupPoliciesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteServiceTemplate(
            self,
            request: models.DeleteServiceTemplateRequest,
            opts: Dict = None,
    ) -> models.DeleteServiceTemplateResponse:
        """
        This API (DeleteServiceTemplate) is used to delete a protocol port template.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteServiceTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteServiceTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteServiceTemplateGroup(
            self,
            request: models.DeleteServiceTemplateGroupRequest,
            opts: Dict = None,
    ) -> models.DeleteServiceTemplateGroupResponse:
        """
        This API (DeleteServiceTemplateGroup) is used to delete a protocol port template group.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteServiceTemplateGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteServiceTemplateGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteSnapshotPolicies(
            self,
            request: models.DeleteSnapshotPoliciesRequest,
            opts: Dict = None,
    ) -> models.DeleteSnapshotPoliciesResponse:
        """
        This API is used to delete snapshot policies.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteSnapshotPolicies"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteSnapshotPoliciesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteSubnet(
            self,
            request: models.DeleteSubnetRequest,
            opts: Dict = None,
    ) -> models.DeleteSubnetResponse:
        """
        This API is used to delete a subnet.
        * Remove all resources in the subnet before deleting it
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteSubnet"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteSubnetResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteTemplateMember(
            self,
            request: models.DeleteTemplateMemberRequest,
            opts: Dict = None,
    ) -> models.DeleteTemplateMemberResponse:
        """
        This API is used to delete a parameter template of the IP address, protocol port, IP address group, or protocol port group type.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteTemplateMember"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteTemplateMemberResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteTrafficPackages(
            self,
            request: models.DeleteTrafficPackagesRequest,
            opts: Dict = None,
    ) -> models.DeleteTrafficPackagesResponse:
        """
        This API is used to delete traffic packages. Note that only non-valid traffic packages can be deleted.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteTrafficPackages"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteTrafficPackagesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteVpc(
            self,
            request: models.DeleteVpcRequest,
            opts: Dict = None,
    ) -> models.DeleteVpcResponse:
        """
        This API (DeleteVpc) is used to delete VPCs.
        * Before deleting a VPC, ensure that the VPC contains no resources, including CVMs, cloud databases, NoSQL databases, VPN gateways, direct connect gateways, load balancers, peering connections, and basic network devices that are linked to the VPC.
        * The deletion of VPCs is irreversible. Proceed with caution.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteVpc"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteVpcResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteVpcEndPoint(
            self,
            request: models.DeleteVpcEndPointRequest,
            opts: Dict = None,
    ) -> models.DeleteVpcEndPointResponse:
        """
        This API is used to delete an endpoint.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteVpcEndPoint"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteVpcEndPointResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteVpcEndPointService(
            self,
            request: models.DeleteVpcEndPointServiceRequest,
            opts: Dict = None,
    ) -> models.DeleteVpcEndPointServiceResponse:
        """
        This API is used to delete an endpoint service.

        """
        
        kwargs = {}
        kwargs["action"] = "DeleteVpcEndPointService"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteVpcEndPointServiceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteVpcEndPointServiceWhiteList(
            self,
            request: models.DeleteVpcEndPointServiceWhiteListRequest,
            opts: Dict = None,
    ) -> models.DeleteVpcEndPointServiceWhiteListResponse:
        """
        This API is used to delete the endpoint service allowlist.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteVpcEndPointServiceWhiteList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteVpcEndPointServiceWhiteListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteVpnConnection(
            self,
            request: models.DeleteVpnConnectionRequest,
            opts: Dict = None,
    ) -> models.DeleteVpnConnectionResponse:
        """
        This API is used to delete a VPN tunnel.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteVpnConnection"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteVpnConnectionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteVpnGateway(
            self,
            request: models.DeleteVpnGatewayRequest,
            opts: Dict = None,
    ) -> models.DeleteVpnGatewayResponse:
        """
        This API (DeleteVpnGateway) is used to delete a VPN gateway. Currently, only deletion of pay-as-you-go IPSEC gateway instances in running status is supported.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteVpnGateway"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteVpnGatewayResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteVpnGatewayRoutes(
            self,
            request: models.DeleteVpnGatewayRoutesRequest,
            opts: Dict = None,
    ) -> models.DeleteVpnGatewayRoutesResponse:
        """
        This API is used to delete routes of a VPN gateway.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteVpnGatewayRoutes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteVpnGatewayRoutesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAccountAttributes(
            self,
            request: models.DescribeAccountAttributesRequest,
            opts: Dict = None,
    ) -> models.DescribeAccountAttributesResponse:
        """
        This API (DescribeAccountAttributes) is used to query your account attributes.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAccountAttributes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAccountAttributesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAddressQuota(
            self,
            request: models.DescribeAddressQuotaRequest,
            opts: Dict = None,
    ) -> models.DescribeAddressQuotaResponse:
        """
        This API (DescribeAddressQuota) is used to query the quota information of your [Elastic IP](https://intl.cloud.tencent.com/document/product/213/1941?from_cn_redirect=1) (EIP) in the current region. For more information, see [EIP product introduction](https://intl.cloud.tencent.com/document/product/213/5733?from_cn_redirect=1).
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAddressQuota"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAddressQuotaResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAddressTemplateGroups(
            self,
            request: models.DescribeAddressTemplateGroupsRequest,
            opts: Dict = None,
    ) -> models.DescribeAddressTemplateGroupsResponse:
        """
        This API (DescribeAddressTemplateGroups) is used to query an IP address template group.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAddressTemplateGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAddressTemplateGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAddressTemplates(
            self,
            request: models.DescribeAddressTemplatesRequest,
            opts: Dict = None,
    ) -> models.DescribeAddressTemplatesResponse:
        """
        This API (DescribeAddressTemplates) is used to query an IP address template.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAddressTemplates"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAddressTemplatesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAddresses(
            self,
            request: models.DescribeAddressesRequest,
            opts: Dict = None,
    ) -> models.DescribeAddressesResponse:
        """
        This API (DescribeAddresses) is used to query the information of one or multiple [Elastic IPs](https://intl.cloud.tencent.com/document/product/213/1941?from_cn_redirect=1).
        * If the parameter is empty, a number (as specified by the `Limit`, the default value is 20) of EIPs will be returned.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAddresses"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAddressesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssistantCidr(
            self,
            request: models.DescribeAssistantCidrRequest,
            opts: Dict = None,
    ) -> models.DescribeAssistantCidrResponse:
        """
        This API is used to query the list of secondary CIDR blocks.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssistantCidr"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssistantCidrResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBandwidthPackageBillUsage(
            self,
            request: models.DescribeBandwidthPackageBillUsageRequest,
            opts: Dict = None,
    ) -> models.DescribeBandwidthPackageBillUsageResponse:
        """
        This API is used to query the current billable usage of a pay-as-you-go bandwidth package.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBandwidthPackageBillUsage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBandwidthPackageBillUsageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBandwidthPackageQuota(
            self,
            request: models.DescribeBandwidthPackageQuotaRequest,
            opts: Dict = None,
    ) -> models.DescribeBandwidthPackageQuotaResponse:
        """
        This API is used to query the maximum and used number of bandwidth packages under the account in the current region.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBandwidthPackageQuota"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBandwidthPackageQuotaResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBandwidthPackageResources(
            self,
            request: models.DescribeBandwidthPackageResourcesRequest,
            opts: Dict = None,
    ) -> models.DescribeBandwidthPackageResourcesResponse:
        """
        This API is used to query the list of resources in a Bandwidth Package according to its unique ID, support conditional filtering of query results and paging query.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBandwidthPackageResources"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBandwidthPackageResourcesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBandwidthPackages(
            self,
            request: models.DescribeBandwidthPackagesRequest,
            opts: Dict = None,
    ) -> models.DescribeBandwidthPackagesResponse:
        """
        This API is used to query bandwidth package information, including the unique ID of the bandwidth package, the type, the billing mode, the name, and the resource information.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBandwidthPackages"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBandwidthPackagesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCcnAttachedInstances(
            self,
            request: models.DescribeCcnAttachedInstancesRequest,
            opts: Dict = None,
    ) -> models.DescribeCcnAttachedInstancesResponse:
        """
        This API (DescribeCcnAttachedInstances) is used to query the network instances associated with the CCN instance.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCcnAttachedInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCcnAttachedInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCcnRegionBandwidthLimits(
            self,
            request: models.DescribeCcnRegionBandwidthLimitsRequest,
            opts: Dict = None,
    ) -> models.DescribeCcnRegionBandwidthLimitsResponse:
        """
        This API is used to query the outbound bandwidth caps of all regions connected with a CCN instance. The API only returns regions included in the associated network instances.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCcnRegionBandwidthLimits"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCcnRegionBandwidthLimitsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCcnRoutes(
            self,
            request: models.DescribeCcnRoutesRequest,
            opts: Dict = None,
    ) -> models.DescribeCcnRoutesResponse:
        """
        This API (DescribeCcnRoutes) is used to query routes that have been added to a CCN.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCcnRoutes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCcnRoutesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCcns(
            self,
            request: models.DescribeCcnsRequest,
            opts: Dict = None,
    ) -> models.DescribeCcnsResponse:
        """
        This API (DescribeCcns) is used to query the CCN list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCcns"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCcnsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClassicLinkInstances(
            self,
            request: models.DescribeClassicLinkInstancesRequest,
            opts: Dict = None,
    ) -> models.DescribeClassicLinkInstancesResponse:
        """
        This API (DescribeClassicLinkInstances) is used to query the Classiclink instances list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClassicLinkInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClassicLinkInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCrossBorderCompliance(
            self,
            request: models.DescribeCrossBorderComplianceRequest,
            opts: Dict = None,
    ) -> models.DescribeCrossBorderComplianceResponse:
        """
        This API is used to query the compliance review requests created by the user.
        A service provider can query all review requests created by any `APPID` under its account. Other users can only query their own review requests.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCrossBorderCompliance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCrossBorderComplianceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCustomerGatewayVendors(
            self,
            request: models.DescribeCustomerGatewayVendorsRequest,
            opts: Dict = None,
    ) -> models.DescribeCustomerGatewayVendorsResponse:
        """
        This API (DescribeCustomerGatewayVendors) is used to query the information of supported customer gateway vendors.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCustomerGatewayVendors"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCustomerGatewayVendorsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCustomerGateways(
            self,
            request: models.DescribeCustomerGatewaysRequest,
            opts: Dict = None,
    ) -> models.DescribeCustomerGatewaysResponse:
        """
        This API (DescribeCustomerGateways) is used to query the customer gateway list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCustomerGateways"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCustomerGatewaysResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDirectConnectGatewayCcnRoutes(
            self,
            request: models.DescribeDirectConnectGatewayCcnRoutesRequest,
            opts: Dict = None,
    ) -> models.DescribeDirectConnectGatewayCcnRoutesResponse:
        """
        This API (DescribeDirectConnectGatewayCcnRoutes) is used to query the CCN routes (IDC IP range) of the Direct Connect gateway.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDirectConnectGatewayCcnRoutes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDirectConnectGatewayCcnRoutesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDirectConnectGateways(
            self,
            request: models.DescribeDirectConnectGatewaysRequest,
            opts: Dict = None,
    ) -> models.DescribeDirectConnectGatewaysResponse:
        """
        This API is used to query direct connect gateways.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDirectConnectGateways"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDirectConnectGatewaysResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeFlowLog(
            self,
            request: models.DescribeFlowLogRequest,
            opts: Dict = None,
    ) -> models.DescribeFlowLogResponse:
        """
        This API is used to query the information of a flow log.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeFlowLog"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeFlowLogResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeFlowLogs(
            self,
            request: models.DescribeFlowLogsRequest,
            opts: Dict = None,
    ) -> models.DescribeFlowLogsResponse:
        """
        This API is used to query all the flow logs of the current account.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeFlowLogs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeFlowLogsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeGatewayFlowMonitorDetail(
            self,
            request: models.DescribeGatewayFlowMonitorDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeGatewayFlowMonitorDetailResponse:
        """
        This API is used to query the traffic monitoring details of the gateway.
        * You can only use this API to query a single gateway instance, which means you must pass in only one of `VpnId`, `DirectConnectGatewayId`, `PeeringConnectionId`, or `NatId`.
        * If the gateway has traffic, but no data is returned when this API is called, please check whether gateway traffic monitoring has been enabled in the corresponding gateway details page in the console.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeGatewayFlowMonitorDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeGatewayFlowMonitorDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeGatewayFlowQos(
            self,
            request: models.DescribeGatewayFlowQosRequest,
            opts: Dict = None,
    ) -> models.DescribeGatewayFlowQosResponse:
        """
        This API is used to query the inbound IP bandwidth limit of a gateway.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeGatewayFlowQos"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeGatewayFlowQosResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeHaVips(
            self,
            request: models.DescribeHaVipsRequest,
            opts: Dict = None,
    ) -> models.DescribeHaVipsResponse:
        """
        This API (DescribeHaVips) is used to query the list of highly available virtual IPs (HAVIP).
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeHaVips"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeHaVipsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeIPv6Addresses(
            self,
            request: models.DescribeIPv6AddressesRequest,
            opts: Dict = None,
    ) -> models.DescribeIPv6AddressesResponse:
        """
        This API is used to query detailed information of one or more EIPv6 instances.

        - You can query EIPv6 and traditional EIPv6 instance information in a specified region.
        - The system returns a certain number (as specified by the Limit, the default value is 20) of EIPv6 instances of the current user if the parameter is empty.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeIPv6Addresses"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeIPv6AddressesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstanceJumbo(
            self,
            request: models.DescribeInstanceJumboRequest,
            opts: Dict = None,
    ) -> models.DescribeInstanceJumboResponse:
        """
        This API is used to check whether Cloud Virtual Machines support jumbo frames.
        Usage limits.
        This API is used to perform operations that require CAM policy authorization and read access to the corresponding instance. The API accesses CVM instances, so it verifies whether there are CAM permissions for the instance. For example: CAM action allows vpc:DescribeInstanceJumbo; resource allows qcs::cvm:ap-guangzhou:uin/2126195383:instance/*.
        This API is used to check the jumbo frame status before and after instance migration. The status returned by this API may be inconsistent before and after migration. You need to check whether the host machines of the instance before and after migration both support jumbo frames. One possible reason is that the instance has been migrated to a host machine that does not support jumbo frames.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstanceJumbo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstanceJumboResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeIp6Addresses(
            self,
            request: models.DescribeIp6AddressesRequest,
            opts: Dict = None,
    ) -> models.DescribeIp6AddressesResponse:
        """
        This API is used to query the detailed information on one or multiple classic elastic public IPv6 instances.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeIp6Addresses"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeIp6AddressesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeIpGeolocationDatabaseUrl(
            self,
            request: models.DescribeIpGeolocationDatabaseUrlRequest,
            opts: Dict = None,
    ) -> models.DescribeIpGeolocationDatabaseUrlResponse:
        """
        This API is used to obtain the download link of an IP location database.
        <font color="#FF0000">This API will be discontinued soon and is only available for existing users.</font>
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeIpGeolocationDatabaseUrl"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeIpGeolocationDatabaseUrlResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeIpGeolocationInfos(
            self,
            request: models.DescribeIpGeolocationInfosRequest,
            opts: Dict = None,
    ) -> models.DescribeIpGeolocationInfosResponse:
        """
        This API is used to query the location and network information of one or more IP addresses.
        <font color="#FF0000">This API will be discontinued soon and is only available for existing users.</font>
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeIpGeolocationInfos"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeIpGeolocationInfosResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLocalGateway(
            self,
            request: models.DescribeLocalGatewayRequest,
            opts: Dict = None,
    ) -> models.DescribeLocalGatewayResponse:
        """
        This API is used to query local gateways of a CDC instance.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLocalGateway"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLocalGatewayResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeNatGatewayDestinationIpPortTranslationNatRules(
            self,
            request: models.DescribeNatGatewayDestinationIpPortTranslationNatRulesRequest,
            opts: Dict = None,
    ) -> models.DescribeNatGatewayDestinationIpPortTranslationNatRulesResponse:
        """
        This API is used to query the array of objects of a NAT gateway's port forwarding rules.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeNatGatewayDestinationIpPortTranslationNatRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeNatGatewayDestinationIpPortTranslationNatRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeNatGatewayDirectConnectGatewayRoute(
            self,
            request: models.DescribeNatGatewayDirectConnectGatewayRouteRequest,
            opts: Dict = None,
    ) -> models.DescribeNatGatewayDirectConnectGatewayRouteResponse:
        """
        This API is used to query the routes between a NAT gateway and Direct Connect.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeNatGatewayDirectConnectGatewayRoute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeNatGatewayDirectConnectGatewayRouteResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeNatGatewaySourceIpTranslationNatRules(
            self,
            request: models.DescribeNatGatewaySourceIpTranslationNatRulesRequest,
            opts: Dict = None,
    ) -> models.DescribeNatGatewaySourceIpTranslationNatRulesResponse:
        """
        This API is used to query the NAT gateway's SNAT forwarding rules.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeNatGatewaySourceIpTranslationNatRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeNatGatewaySourceIpTranslationNatRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeNatGateways(
            self,
            request: models.DescribeNatGatewaysRequest,
            opts: Dict = None,
    ) -> models.DescribeNatGatewaysResponse:
        """
        This API is used to query NAT gateways.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeNatGateways"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeNatGatewaysResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeNetDetectStates(
            self,
            request: models.DescribeNetDetectStatesRequest,
            opts: Dict = None,
    ) -> models.DescribeNetDetectStatesResponse:
        """
        This API (DescribeNetDetectStates) is used to query the list of network detection verification results.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeNetDetectStates"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeNetDetectStatesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeNetDetects(
            self,
            request: models.DescribeNetDetectsRequest,
            opts: Dict = None,
    ) -> models.DescribeNetDetectsResponse:
        """
        This API (DescribeNetDetects) is used to query the list of network detection instances.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeNetDetects"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeNetDetectsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeNetworkAclQuintupleEntries(
            self,
            request: models.DescribeNetworkAclQuintupleEntriesRequest,
            opts: Dict = None,
    ) -> models.DescribeNetworkAclQuintupleEntriesResponse:
        """
        This API is used to query the list of in/outbound network ACL quintuple entries.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeNetworkAclQuintupleEntries"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeNetworkAclQuintupleEntriesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeNetworkAcls(
            self,
            request: models.DescribeNetworkAclsRequest,
            opts: Dict = None,
    ) -> models.DescribeNetworkAclsResponse:
        """
        This API is used to query a list of network ACLs.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeNetworkAcls"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeNetworkAclsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeNetworkInterfaceLimit(
            self,
            request: models.DescribeNetworkInterfaceLimitRequest,
            opts: Dict = None,
    ) -> models.DescribeNetworkInterfaceLimitResponse:
        """
        This API (DescribeNetworkInterfaceLimit) is used to query the ENI quota based on the ID of CVM instance or ENI. It returns the ENI quota to which the CVM instance can be bound and the IP address quota that can be allocated to the ENI.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeNetworkInterfaceLimit"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeNetworkInterfaceLimitResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeNetworkInterfaces(
            self,
            request: models.DescribeNetworkInterfacesRequest,
            opts: Dict = None,
    ) -> models.DescribeNetworkInterfacesResponse:
        """
        This API (DescribeNetworkInterfaces) is used to query the ENI list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeNetworkInterfaces"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeNetworkInterfacesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeReserveIpAddresses(
            self,
            request: models.DescribeReserveIpAddressesRequest,
            opts: Dict = None,
    ) -> models.DescribeReserveIpAddressesResponse:
        """
        This API is used to query reserved private IP addresses.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeReserveIpAddresses"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeReserveIpAddressesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRoutePolicyEntries(
            self,
            request: models.DescribeRoutePolicyEntriesRequest,
            opts: Dict = None,
    ) -> models.DescribeRoutePolicyEntriesResponse:
        """
        This API is used to query the route reception policy entry list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRoutePolicyEntries"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRoutePolicyEntriesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRouteTables(
            self,
            request: models.DescribeRouteTablesRequest,
            opts: Dict = None,
    ) -> models.DescribeRouteTablesResponse:
        """
        This API is used to query route tables.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRouteTables"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRouteTablesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSecurityGroupAssociationStatistics(
            self,
            request: models.DescribeSecurityGroupAssociationStatisticsRequest,
            opts: Dict = None,
    ) -> models.DescribeSecurityGroupAssociationStatisticsResponse:
        """
        This API (DescribeSecurityGroupAssociationStatistics) is used to query statistics on the instances associated with a security group.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSecurityGroupAssociationStatistics"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSecurityGroupAssociationStatisticsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSecurityGroupPolicies(
            self,
            request: models.DescribeSecurityGroupPoliciesRequest,
            opts: Dict = None,
    ) -> models.DescribeSecurityGroupPoliciesResponse:
        """
        This API (DescribeSecurityGroupPolicies) is used to query security group policies.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSecurityGroupPolicies"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSecurityGroupPoliciesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSecurityGroupReferences(
            self,
            request: models.DescribeSecurityGroupReferencesRequest,
            opts: Dict = None,
    ) -> models.DescribeSecurityGroupReferencesResponse:
        """
        This API (DescribeSecurityGroupReferences) is used to query referred security groups.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSecurityGroupReferences"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSecurityGroupReferencesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSecurityGroups(
            self,
            request: models.DescribeSecurityGroupsRequest,
            opts: Dict = None,
    ) -> models.DescribeSecurityGroupsResponse:
        """
        This API (DescribeSecurityGroups) is used to query security groups.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSecurityGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSecurityGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeServiceTemplateGroups(
            self,
            request: models.DescribeServiceTemplateGroupsRequest,
            opts: Dict = None,
    ) -> models.DescribeServiceTemplateGroupsResponse:
        """
        This API (DescribeServiceTemplateGroups) is used to query a protocol port template group.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeServiceTemplateGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeServiceTemplateGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeServiceTemplates(
            self,
            request: models.DescribeServiceTemplatesRequest,
            opts: Dict = None,
    ) -> models.DescribeServiceTemplatesResponse:
        """
        This API (DescribeServiceTemplates) is used to query protocol port templates.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeServiceTemplates"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeServiceTemplatesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSgSnapshotFileContent(
            self,
            request: models.DescribeSgSnapshotFileContentRequest,
            opts: Dict = None,
    ) -> models.DescribeSgSnapshotFileContentResponse:
        """
        This API is used to query the snapshot file contents.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSgSnapshotFileContent"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSgSnapshotFileContentResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSnapshotAttachedInstances(
            self,
            request: models.DescribeSnapshotAttachedInstancesRequest,
            opts: Dict = None,
    ) -> models.DescribeSnapshotAttachedInstancesResponse:
        """
        This API is used to query instances associated with a snapshot policy.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSnapshotAttachedInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSnapshotAttachedInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSnapshotFiles(
            self,
            request: models.DescribeSnapshotFilesRequest,
            opts: Dict = None,
    ) -> models.DescribeSnapshotFilesResponse:
        """
        This API is used to query snapshot files.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSnapshotFiles"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSnapshotFilesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSnapshotPolicies(
            self,
            request: models.DescribeSnapshotPoliciesRequest,
            opts: Dict = None,
    ) -> models.DescribeSnapshotPoliciesResponse:
        """
        This API is used to query snapshot policies.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSnapshotPolicies"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSnapshotPoliciesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSubnetResourceDashboard(
            self,
            request: models.DescribeSubnetResourceDashboardRequest,
            opts: Dict = None,
    ) -> models.DescribeSubnetResourceDashboardResponse:
        """
        This API is used to query the subnet resource.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSubnetResourceDashboard"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSubnetResourceDashboardResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSubnets(
            self,
            request: models.DescribeSubnetsRequest,
            opts: Dict = None,
    ) -> models.DescribeSubnetsResponse:
        """
        This API (DescribeSubnets) is used to query the list of subnets.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSubnets"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSubnetsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTaskResult(
            self,
            request: models.DescribeTaskResultRequest,
            opts: Dict = None,
    ) -> models.DescribeTaskResultResponse:
        """
        This API is used to query the EIP async job execution results.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTaskResult"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTaskResultResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTrafficPackages(
            self,
            request: models.DescribeTrafficPackagesRequest,
            opts: Dict = None,
    ) -> models.DescribeTrafficPackagesResponse:
        """
        This API is used to query the details of shared traffic packages.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTrafficPackages"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTrafficPackagesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUsedIpAddress(
            self,
            request: models.DescribeUsedIpAddressRequest,
            opts: Dict = None,
    ) -> models.DescribeUsedIpAddressResponse:
        """
        This API is used to query the IP usage of a subnet or VPC.
        If the IP is occupied, the resource type and ID associated with the are is returned. If the IP is not used, it returns null.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUsedIpAddress"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUsedIpAddressResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVpcEndPoint(
            self,
            request: models.DescribeVpcEndPointRequest,
            opts: Dict = None,
    ) -> models.DescribeVpcEndPointResponse:
        """
        This API is used to query the endpoint list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVpcEndPoint"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVpcEndPointResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVpcEndPointService(
            self,
            request: models.DescribeVpcEndPointServiceRequest,
            opts: Dict = None,
    ) -> models.DescribeVpcEndPointServiceResponse:
        """
        This API is used to query the endpoint service list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVpcEndPointService"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVpcEndPointServiceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVpcEndPointServiceWhiteList(
            self,
            request: models.DescribeVpcEndPointServiceWhiteListRequest,
            opts: Dict = None,
    ) -> models.DescribeVpcEndPointServiceWhiteListResponse:
        """
        This API is used to query the endpoint service allowlist.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVpcEndPointServiceWhiteList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVpcEndPointServiceWhiteListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVpcInstances(
            self,
            request: models.DescribeVpcInstancesRequest,
            opts: Dict = None,
    ) -> models.DescribeVpcInstancesResponse:
        """
        This API (DescribeVpcInstances) is used to query a list of VCM instances on VPC.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVpcInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVpcInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVpcIpv6Addresses(
            self,
            request: models.DescribeVpcIpv6AddressesRequest,
            opts: Dict = None,
    ) -> models.DescribeVpcIpv6AddressesResponse:
        """
        This API (DescribeVpcIpv6Addresses) is used to query `VPC` `IPv6` information.
        This API is used to query only the information of `IPv6` addresses that are already in use. When querying IPs that have not yet been used, this API will not report an error, but the IPs will not appear in the returned results.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVpcIpv6Addresses"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVpcIpv6AddressesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVpcPrivateIpAddresses(
            self,
            request: models.DescribeVpcPrivateIpAddressesRequest,
            opts: Dict = None,
    ) -> models.DescribeVpcPrivateIpAddressesResponse:
        """
        This API (DescribeVpcPrivateIpAddresses) is used to query the private IP information of a VPC.<br />
        This API is used to query only the information of IP addresses that are already in use. When querying IPs that have not yet been used, this API will not report an error, but the IPs will not appear in the returned results.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVpcPrivateIpAddresses"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVpcPrivateIpAddressesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVpcResourceDashboard(
            self,
            request: models.DescribeVpcResourceDashboardRequest,
            opts: Dict = None,
    ) -> models.DescribeVpcResourceDashboardResponse:
        """
        View VPC resources.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVpcResourceDashboard"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVpcResourceDashboardResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVpcTaskResult(
            self,
            request: models.DescribeVpcTaskResultRequest,
            opts: Dict = None,
    ) -> models.DescribeVpcTaskResultResponse:
        """
        This API is used to query the execution result of a VPC task.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVpcTaskResult"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVpcTaskResultResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVpcs(
            self,
            request: models.DescribeVpcsRequest,
            opts: Dict = None,
    ) -> models.DescribeVpcsResponse:
        """
        This API (DescribeVpcs) is used to query the VPC list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVpcs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVpcsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVpnConnections(
            self,
            request: models.DescribeVpnConnectionsRequest,
            opts: Dict = None,
    ) -> models.DescribeVpnConnectionsResponse:
        """
        This API is used to used to query the list of VPN tunnels.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVpnConnections"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVpnConnectionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVpnGatewayCcnRoutes(
            self,
            request: models.DescribeVpnGatewayCcnRoutesRequest,
            opts: Dict = None,
    ) -> models.DescribeVpnGatewayCcnRoutesResponse:
        """
        This API is used to query VPN gateway-based CCN routes.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVpnGatewayCcnRoutes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVpnGatewayCcnRoutesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVpnGatewayRoutes(
            self,
            request: models.DescribeVpnGatewayRoutesRequest,
            opts: Dict = None,
    ) -> models.DescribeVpnGatewayRoutesResponse:
        """
        This API is used to query VPN gateway routes.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVpnGatewayRoutes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVpnGatewayRoutesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVpnGateways(
            self,
            request: models.DescribeVpnGatewaysRequest,
            opts: Dict = None,
    ) -> models.DescribeVpnGatewaysResponse:
        """
        This API (DescribeVpnGateways) is used to query the VPN gateway list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVpnGateways"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVpnGatewaysResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DetachCcnInstances(
            self,
            request: models.DetachCcnInstancesRequest,
            opts: Dict = None,
    ) -> models.DetachCcnInstancesResponse:
        """
        This API (DetachCcnInstances) is used to unbind a specified network instance from a CCN instance.<br />
        After unbinding the network instance, the corresponding routing policy will also be deleted.
        """
        
        kwargs = {}
        kwargs["action"] = "DetachCcnInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DetachCcnInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DetachClassicLinkVpc(
            self,
            request: models.DetachClassicLinkVpcRequest,
            opts: Dict = None,
    ) -> models.DetachClassicLinkVpcResponse:
        """
        This API is used to delete a Classiclink.
        >?This API is async. You can call the [`DescribeVpcTaskResult`](https://intl.cloud.tencent.com/document/api/215/59037?from_cn_redirect=1) API to query the task result. When the task is completed, you can continue other tasks.
        >
        """
        
        kwargs = {}
        kwargs["action"] = "DetachClassicLinkVpc"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DetachClassicLinkVpcResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DetachNetworkInterface(
            self,
            request: models.DetachNetworkInterfaceRequest,
            opts: Dict = None,
    ) -> models.DetachNetworkInterfaceResponse:
        """
        This API is used to unbind an ENI from a CVM.
        This API is completed asynchronously. If you need to query the execution result of an async task, please use the `RequestId` returned by this API to poll the `DescribeVpcTaskResult` API.
        """
        
        kwargs = {}
        kwargs["action"] = "DetachNetworkInterface"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DetachNetworkInterfaceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DetachSnapshotInstances(
            self,
            request: models.DetachSnapshotInstancesRequest,
            opts: Dict = None,
    ) -> models.DetachSnapshotInstancesResponse:
        """
        This API is used to disassociate a snapshot policy with instances.
        """
        
        kwargs = {}
        kwargs["action"] = "DetachSnapshotInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DetachSnapshotInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DisableCcnRoutes(
            self,
            request: models.DisableCcnRoutesRequest,
            opts: Dict = None,
    ) -> models.DisableCcnRoutesResponse:
        """
        This API (DisableCcnRoutes) is used to disable CCN routes that are already enabled.
        """
        
        kwargs = {}
        kwargs["action"] = "DisableCcnRoutes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DisableCcnRoutesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DisableFlowLogs(
            self,
            request: models.DisableFlowLogsRequest,
            opts: Dict = None,
    ) -> models.DisableFlowLogsResponse:
        """
        This API is used to disable flow log.
        """
        
        kwargs = {}
        kwargs["action"] = "DisableFlowLogs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DisableFlowLogsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DisableGatewayFlowMonitor(
            self,
            request: models.DisableGatewayFlowMonitorRequest,
            opts: Dict = None,
    ) -> models.DisableGatewayFlowMonitorResponse:
        """
        This API is used to disable gateway traffic monitor.
        """
        
        kwargs = {}
        kwargs["action"] = "DisableGatewayFlowMonitor"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DisableGatewayFlowMonitorResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DisableRoutes(
            self,
            request: models.DisableRoutesRequest,
            opts: Dict = None,
    ) -> models.DisableRoutesResponse:
        """
        This API is used to disable enabled subnet routes.
        """
        
        kwargs = {}
        kwargs["action"] = "DisableRoutes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DisableRoutesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DisableSnapshotPolicies(
            self,
            request: models.DisableSnapshotPoliciesRequest,
            opts: Dict = None,
    ) -> models.DisableSnapshotPoliciesResponse:
        """
        This API is used to disable specified snapshot policies.
        """
        
        kwargs = {}
        kwargs["action"] = "DisableSnapshotPolicies"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DisableSnapshotPoliciesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DisassociateAddress(
            self,
            request: models.DisassociateAddressRequest,
            opts: Dict = None,
    ) -> models.DisassociateAddressResponse:
        """
        This API is used to unbind an [Elastic IP](https://intl.cloud.tencent.com/document/product/213/1941?from_cn_redirect=1) (EIP for short).
        * This API supports unbinding an EIP from CVM instances and ENIs.
        * This API does not support unbinding an EIP from a NAT Gateway. To unbind an EIP from a NAT Gateway, use the [`DisassociateNatGatewayAddress`](https://intl.cloud.tencent.com/document/api/215/36716?from_cn_redirect=1) API.
        * Only EIPs in BIND or BIND_ENI status can be unbound.
        * Blocked EIPs cannot be unbound.
        """
        
        kwargs = {}
        kwargs["action"] = "DisassociateAddress"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DisassociateAddressResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DisassociateDirectConnectGatewayNatGateway(
            self,
            request: models.DisassociateDirectConnectGatewayNatGatewayRequest,
            opts: Dict = None,
    ) -> models.DisassociateDirectConnectGatewayNatGatewayResponse:
        """
        This API is used to unbind a direct connect gateway from a NAT Gateway. After unbinding, the direct connect gateway cannot access internet through the NAT Gateway.
        """
        
        kwargs = {}
        kwargs["action"] = "DisassociateDirectConnectGatewayNatGateway"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DisassociateDirectConnectGatewayNatGatewayResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DisassociateIPv6Address(
            self,
            request: models.DisassociateIPv6AddressRequest,
            opts: Dict = None,
    ) -> models.DisassociateIPv6AddressResponse:
        """
        This API is used to unbind an EIPv6 instance.

        - You can unbind EIPv6 instances bound to Cloud Virtual Machine (CVM) or Elastic Network Interface (ENI).
        - Only EIPv6 instances in BIND or BIND_ENI status can be unbound.
        """
        
        kwargs = {}
        kwargs["action"] = "DisassociateIPv6Address"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DisassociateIPv6AddressResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DisassociateNatGatewayAddress(
            self,
            request: models.DisassociateNatGatewayAddressRequest,
            opts: Dict = None,
    ) -> models.DisassociateNatGatewayAddressResponse:
        """
        This API is used to unbind an EIP from a NAT gateway.
        """
        
        kwargs = {}
        kwargs["action"] = "DisassociateNatGatewayAddress"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DisassociateNatGatewayAddressResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DisassociateNetworkAclSubnets(
            self,
            request: models.DisassociateNetworkAclSubnetsRequest,
            opts: Dict = None,
    ) -> models.DisassociateNetworkAclSubnetsResponse:
        """
        This API is used to disassociate a network ACL from subnets in a VPC instance.
        """
        
        kwargs = {}
        kwargs["action"] = "DisassociateNetworkAclSubnets"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DisassociateNetworkAclSubnetsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DisassociateNetworkInterfaceSecurityGroups(
            self,
            request: models.DisassociateNetworkInterfaceSecurityGroupsRequest,
            opts: Dict = None,
    ) -> models.DisassociateNetworkInterfaceSecurityGroupsResponse:
        """
        This API (DisassociateNetworkInterfaceSecurityGroups) is used to detach (or fully detach if possible) a security group from an ENI.
        """
        
        kwargs = {}
        kwargs["action"] = "DisassociateNetworkInterfaceSecurityGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DisassociateNetworkInterfaceSecurityGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DisassociateVpcEndPointSecurityGroups(
            self,
            request: models.DisassociateVpcEndPointSecurityGroupsRequest,
            opts: Dict = None,
    ) -> models.DisassociateVpcEndPointSecurityGroupsResponse:
        """
        This API is used to unbind an endpoint from a security group.
        """
        
        kwargs = {}
        kwargs["action"] = "DisassociateVpcEndPointSecurityGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DisassociateVpcEndPointSecurityGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DownloadCustomerGatewayConfiguration(
            self,
            request: models.DownloadCustomerGatewayConfigurationRequest,
            opts: Dict = None,
    ) -> models.DownloadCustomerGatewayConfigurationResponse:
        """
        This API is used to download VPN tunnel configurations.
        """
        
        kwargs = {}
        kwargs["action"] = "DownloadCustomerGatewayConfiguration"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DownloadCustomerGatewayConfigurationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def EnableCcnRoutes(
            self,
            request: models.EnableCcnRoutesRequest,
            opts: Dict = None,
    ) -> models.EnableCcnRoutesResponse:
        """
        This API (EnableCcnRoutes) is used to enable CCN routes that are already added.<br />
        This API is used to verify whether there will be conflict with an existing route after a CCN route is enabled. If there is a conflict, the route will not be enabled, and the process will fail. When a conflict occurs, you must disable the conflicting route before you can enable the desired route.
        """
        
        kwargs = {}
        kwargs["action"] = "EnableCcnRoutes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.EnableCcnRoutesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def EnableFlowLogs(
            self,
            request: models.EnableFlowLogsRequest,
            opts: Dict = None,
    ) -> models.EnableFlowLogsResponse:
        """
        This API is used to enable flow log.
        """
        
        kwargs = {}
        kwargs["action"] = "EnableFlowLogs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.EnableFlowLogsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def EnableGatewayFlowMonitor(
            self,
            request: models.EnableGatewayFlowMonitorRequest,
            opts: Dict = None,
    ) -> models.EnableGatewayFlowMonitorResponse:
        """
        This API is used to enable gateway traffic monitor.
        """
        
        kwargs = {}
        kwargs["action"] = "EnableGatewayFlowMonitor"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.EnableGatewayFlowMonitorResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def EnableRoutes(
            self,
            request: models.EnableRoutesRequest,
            opts: Dict = None,
    ) -> models.EnableRoutesResponse:
        """
        This API is used to enable disabled subnet routes.<br />
        The API is used to verify whether the enabled route conflicts with existing routes. If they conflict, the new route cannot be enabled and will result in a failure. When a route conflict occurs, you need to first disable the conflicting route before you can enable the new one.
        """
        
        kwargs = {}
        kwargs["action"] = "EnableRoutes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.EnableRoutesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def EnableSnapshotPolicies(
            self,
            request: models.EnableSnapshotPoliciesRequest,
            opts: Dict = None,
    ) -> models.EnableSnapshotPoliciesResponse:
        """
        This API is used to enable specified snapshot policies.
        """
        
        kwargs = {}
        kwargs["action"] = "EnableSnapshotPolicies"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.EnableSnapshotPoliciesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def EnableVpcEndPointConnect(
            self,
            request: models.EnableVpcEndPointConnectRequest,
            opts: Dict = None,
    ) -> models.EnableVpcEndPointConnectResponse:
        """
        This API is used to determine whether to accept the request of connecting with an endpoint.
        """
        
        kwargs = {}
        kwargs["action"] = "EnableVpcEndPointConnect"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.EnableVpcEndPointConnectResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GenerateVpnConnectionDefaultHealthCheckIp(
            self,
            request: models.GenerateVpnConnectionDefaultHealthCheckIpRequest,
            opts: Dict = None,
    ) -> models.GenerateVpnConnectionDefaultHealthCheckIpResponse:
        """
        This API is used to get a pair of VPN tunnel health check addresses.
        """
        
        kwargs = {}
        kwargs["action"] = "GenerateVpnConnectionDefaultHealthCheckIp"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GenerateVpnConnectionDefaultHealthCheckIpResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetCcnRegionBandwidthLimits(
            self,
            request: models.GetCcnRegionBandwidthLimitsRequest,
            opts: Dict = None,
    ) -> models.GetCcnRegionBandwidthLimitsResponse:
        """
        This API is used to query the bandwidth limits of a CCN instance. Monthly-subscribed CCNs only support Inter-region Bandwidth Limits, while the pay-as-you-go CCNs support both the Inter-region Bandwidth Limits and Region Outbound Bandwidth Limits.
        """
        
        kwargs = {}
        kwargs["action"] = "GetCcnRegionBandwidthLimits"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetCcnRegionBandwidthLimitsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def HaVipAssociateAddressIp(
            self,
            request: models.HaVipAssociateAddressIpRequest,
            opts: Dict = None,
    ) -> models.HaVipAssociateAddressIpResponse:
        """
        This API is used to bind an EIP to an HAVIP. <br />
        This API is completed asynchronously. If you need to query the execution result of an async task, please use the `RequestId` returned by this API to poll the `DescribeVpcTaskResult` API.
        """
        
        kwargs = {}
        kwargs["action"] = "HaVipAssociateAddressIp"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.HaVipAssociateAddressIpResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def HaVipDisassociateAddressIp(
            self,
            request: models.HaVipDisassociateAddressIpRequest,
            opts: Dict = None,
    ) -> models.HaVipDisassociateAddressIpResponse:
        """
        This API is used to unbind an EIP from an HAVIP. <br />
        This API is completed asynchronously. If you need to query the execution result of an async task, please use the `RequestId` returned by this API to poll the `DescribeVpcTaskResult` API.
        """
        
        kwargs = {}
        kwargs["action"] = "HaVipDisassociateAddressIp"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.HaVipDisassociateAddressIpResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def InquirePriceCreateDirectConnectGateway(
            self,
            request: models.InquirePriceCreateDirectConnectGatewayRequest,
            opts: Dict = None,
    ) -> models.InquirePriceCreateDirectConnectGatewayResponse:
        """
        This API is used to query the price of creating a direct connect gateway.
        """
        
        kwargs = {}
        kwargs["action"] = "InquirePriceCreateDirectConnectGateway"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.InquirePriceCreateDirectConnectGatewayResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def InquiryPriceAllocateAddresses(
            self,
            request: models.InquiryPriceAllocateAddressesRequest,
            opts: Dict = None,
    ) -> models.InquiryPriceAllocateAddressesResponse:
        """
        This API (InquiryPriceAllocateAddresses) is used to query the price of purchasing EIPs.
        """
        
        kwargs = {}
        kwargs["action"] = "InquiryPriceAllocateAddresses"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.InquiryPriceAllocateAddressesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def InquiryPriceModifyAddressesBandwidth(
            self,
            request: models.InquiryPriceModifyAddressesBandwidthRequest,
            opts: Dict = None,
    ) -> models.InquiryPriceModifyAddressesBandwidthResponse:
        """
        This API is used to query the price of modifying EIP bandwidth.
        """
        
        kwargs = {}
        kwargs["action"] = "InquiryPriceModifyAddressesBandwidth"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.InquiryPriceModifyAddressesBandwidthResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def InquiryPriceRenewAddresses(
            self,
            request: models.InquiryPriceRenewAddressesRequest,
            opts: Dict = None,
    ) -> models.InquiryPriceRenewAddressesResponse:
        """
        This API (InquiryPriceRenewAddresses) is used to query the price of renewing prepaid EIPs.
        """
        
        kwargs = {}
        kwargs["action"] = "InquiryPriceRenewAddresses"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.InquiryPriceRenewAddressesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def InquiryPriceRenewVpnGateway(
            self,
            request: models.InquiryPriceRenewVpnGatewayRequest,
            opts: Dict = None,
    ) -> models.InquiryPriceRenewVpnGatewayResponse:
        """
        This API (InquiryPriceRenewVpnGateway) is used to query the price for VPN gateway renewal. Currently, only querying prices for IPSEC-type gateways is supported.
        """
        
        kwargs = {}
        kwargs["action"] = "InquiryPriceRenewVpnGateway"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.InquiryPriceRenewVpnGatewayResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def InquiryPriceResetVpnGatewayInternetMaxBandwidth(
            self,
            request: models.InquiryPriceResetVpnGatewayInternetMaxBandwidthRequest,
            opts: Dict = None,
    ) -> models.InquiryPriceResetVpnGatewayInternetMaxBandwidthResponse:
        """
        This API (InquiryPriceResetVpnGatewayInternetMaxBandwidth) is used to query the price for adjusting the bandwidth cap of a VPN gateway.
        """
        
        kwargs = {}
        kwargs["action"] = "InquiryPriceResetVpnGatewayInternetMaxBandwidth"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.InquiryPriceResetVpnGatewayInternetMaxBandwidthResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def MigrateNetworkInterface(
            self,
            request: models.MigrateNetworkInterfaceRequest,
            opts: Dict = None,
    ) -> models.MigrateNetworkInterfaceResponse:
        """
        This API is used to migrate ENIs.
        This API is completed asynchronously. If you need to query the execution result of an async task, please use the `RequestId` returned by this API to poll the `DescribeVpcTaskResult` API.
        """
        
        kwargs = {}
        kwargs["action"] = "MigrateNetworkInterface"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.MigrateNetworkInterfaceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def MigratePrivateIpAddress(
            self,
            request: models.MigratePrivateIpAddressRequest,
            opts: Dict = None,
    ) -> models.MigratePrivateIpAddressResponse:
        """
        This API is used to migrate the private IPs between ENIs.
        * Note that primary IPs cannot be migrated.
        * The source and destination ENI must be within the same subnet.

        This API is completed asynchronously. If you need to query the execution result of an async task, please use the `RequestId` returned by this API to poll the `DescribeVpcTaskResult` API.
        """
        
        kwargs = {}
        kwargs["action"] = "MigratePrivateIpAddress"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.MigratePrivateIpAddressResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAddressAttribute(
            self,
            request: models.ModifyAddressAttributeRequest,
            opts: Dict = None,
    ) -> models.ModifyAddressAttributeResponse:
        """
        This API (ModifyAddressAttribute) is used to modify the name of an [Elastic IP](https://intl.cloud.tencent.com/document/product/213/1941?from_cn_redirect=1).
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAddressAttribute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAddressAttributeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAddressInternetChargeType(
            self,
            request: models.ModifyAddressInternetChargeTypeRequest,
            opts: Dict = None,
    ) -> models.ModifyAddressInternetChargeTypeResponse:
        """
        This API is used to adjust the network billing mode of an EIP. Please note that it's available to users whose network fees are billed on IPs but not CVMs.
        * The network billing mode can be switched between `BANDWIDTH_PREPAID_BY_MONTH` and `TRAFFIC_POSTPAID_BY_HOUR`.
        * The network billing mode for each EIP be changed for up to twice.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAddressInternetChargeType"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAddressInternetChargeTypeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAddressTemplateAttribute(
            self,
            request: models.ModifyAddressTemplateAttributeRequest,
            opts: Dict = None,
    ) -> models.ModifyAddressTemplateAttributeResponse:
        """
        This API (ModifyAddressTemplateAttribute) is used to modify an IP address template.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAddressTemplateAttribute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAddressTemplateAttributeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAddressTemplateGroupAttribute(
            self,
            request: models.ModifyAddressTemplateGroupAttributeRequest,
            opts: Dict = None,
    ) -> models.ModifyAddressTemplateGroupAttributeResponse:
        """
        This API (ModifyAddressTemplateGroupAttribute) is used to modify an IP address template group.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAddressTemplateGroupAttribute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAddressTemplateGroupAttributeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAddressesBandwidth(
            self,
            request: models.ModifyAddressesBandwidthRequest,
            opts: Dict = None,
    ) -> models.ModifyAddressesBandwidthResponse:
        """
        This API is used to adjust the bandwidth of [Elastic IP](https://intl.cloud.tencent.com/document/product/213/1941?from_cn_redirect=1), including EIP billed on a pay-as-you-go, monthly subscription, and bandwidth package basis.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAddressesBandwidth"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAddressesBandwidthResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAddressesRenewFlag(
            self,
            request: models.ModifyAddressesRenewFlagRequest,
            opts: Dict = None,
    ) -> models.ModifyAddressesRenewFlagResponse:
        """
        This API is used to adjust the renewal flag for the monthly subscription EIP.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAddressesRenewFlag"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAddressesRenewFlagResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAssistantCidr(
            self,
            request: models.ModifyAssistantCidrRequest,
            opts: Dict = None,
    ) -> models.ModifyAssistantCidrResponse:
        """
        This API is used to batch modify (add or delete) secondary CIDR blocks.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAssistantCidr"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAssistantCidrResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyBandwidthPackageAttribute(
            self,
            request: models.ModifyBandwidthPackageAttributeRequest,
            opts: Dict = None,
    ) -> models.ModifyBandwidthPackageAttributeResponse:
        """
        This API is used to modify the attributes of a bandwidth package, including the bandwidth package name, and so on.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyBandwidthPackageAttribute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyBandwidthPackageAttributeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyBandwidthPackageBandwidth(
            self,
            request: models.ModifyBandwidthPackageBandwidthRequest,
            opts: Dict = None,
    ) -> models.ModifyBandwidthPackageBandwidthResponse:
        """
        This API is used to adjust the bandwidth of a [bandwidth package](https://www.tencentcloud.com/document/product/684/15245).
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyBandwidthPackageBandwidth"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyBandwidthPackageBandwidthResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyCcnAttachedInstancesAttribute(
            self,
            request: models.ModifyCcnAttachedInstancesAttributeRequest,
            opts: Dict = None,
    ) -> models.ModifyCcnAttachedInstancesAttributeResponse:
        """
        This API is used to modify CCN-associated instance attributes. Currently, only the `description` can be modified.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyCcnAttachedInstancesAttribute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyCcnAttachedInstancesAttributeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyCcnAttribute(
            self,
            request: models.ModifyCcnAttributeRequest,
            opts: Dict = None,
    ) -> models.ModifyCcnAttributeResponse:
        """
        This API (ModifyCcnAttribute) is used to modify CCN attributes.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyCcnAttribute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyCcnAttributeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyCcnRegionBandwidthLimitsType(
            self,
            request: models.ModifyCcnRegionBandwidthLimitsTypeRequest,
            opts: Dict = None,
    ) -> models.ModifyCcnRegionBandwidthLimitsTypeResponse:
        """
        This API is used to modify the bandwidth limit policy of a postpaid CCN instance.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyCcnRegionBandwidthLimitsType"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyCcnRegionBandwidthLimitsTypeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyCustomerGatewayAttribute(
            self,
            request: models.ModifyCustomerGatewayAttributeRequest,
            opts: Dict = None,
    ) -> models.ModifyCustomerGatewayAttributeResponse:
        """
        This API (ModifyCustomerGatewayAttribute) is used to modify the customer gateway information.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyCustomerGatewayAttribute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyCustomerGatewayAttributeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDirectConnectGatewayAttribute(
            self,
            request: models.ModifyDirectConnectGatewayAttributeRequest,
            opts: Dict = None,
    ) -> models.ModifyDirectConnectGatewayAttributeResponse:
        """
        This API is used to modify the attributes of a direct connect gateway.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDirectConnectGatewayAttribute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDirectConnectGatewayAttributeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyFlowLogAttribute(
            self,
            request: models.ModifyFlowLogAttributeRequest,
            opts: Dict = None,
    ) -> models.ModifyFlowLogAttributeResponse:
        """
        This API is used to modify the attributes of a flow log.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyFlowLogAttribute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyFlowLogAttributeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyGatewayFlowQos(
            self,
            request: models.ModifyGatewayFlowQosRequest,
            opts: Dict = None,
    ) -> models.ModifyGatewayFlowQosResponse:
        """
        This API is used to adjust the bandwidth limit of a gateway.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyGatewayFlowQos"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyGatewayFlowQosResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyHaVipAttribute(
            self,
            request: models.ModifyHaVipAttributeRequest,
            opts: Dict = None,
    ) -> models.ModifyHaVipAttributeResponse:
        """
        This API (ModifyHaVipAttribute) is used to modify HAVIP attributes.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyHaVipAttribute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyHaVipAttributeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyIPv6AddressesAttributes(
            self,
            request: models.ModifyIPv6AddressesAttributesRequest,
            opts: Dict = None,
    ) -> models.ModifyIPv6AddressesAttributesResponse:
        """
        This API is used to modify the name of an EIPv6 instance.

        - You can modify the name of both EIPv6 and traditional EIPv6 instances.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyIPv6AddressesAttributes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyIPv6AddressesAttributesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyIPv6AddressesBandwidth(
            self,
            request: models.ModifyIPv6AddressesBandwidthRequest,
            opts: Dict = None,
    ) -> models.ModifyIPv6AddressesBandwidthResponse:
        """
        This API is used to modify the bandwidth cap of an EIPv6 instance.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyIPv6AddressesBandwidth"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyIPv6AddressesBandwidthResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyIp6AddressesBandwidth(
            self,
            request: models.ModifyIp6AddressesBandwidthRequest,
            opts: Dict = None,
    ) -> models.ModifyIp6AddressesBandwidthResponse:
        """
        This API is used to adjust the bandwidth limit of a classic elastic public IPv6 instance.

        - You can adjust the bandwidth limit of only classic elastic public IPv6 instances.
        - To adjust the bandwidth limit of an elastic public IPv6 instance, call the ModifyIPv6AddressesBandwidth API.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyIp6AddressesBandwidth"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyIp6AddressesBandwidthResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyIpv6AddressesAttribute(
            self,
            request: models.ModifyIpv6AddressesAttributeRequest,
            opts: Dict = None,
    ) -> models.ModifyIpv6AddressesAttributeResponse:
        """
        This API (ModifyIpv6AddressesAttribute) is used to modify the private IPv6 address attributes of an ENI.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyIpv6AddressesAttribute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyIpv6AddressesAttributeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyLocalGateway(
            self,
            request: models.ModifyLocalGatewayRequest,
            opts: Dict = None,
    ) -> models.ModifyLocalGatewayResponse:
        """
        This API is used to modify the local gateway of a CDC instance.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyLocalGateway"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyLocalGatewayResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyNatGatewayAttribute(
            self,
            request: models.ModifyNatGatewayAttributeRequest,
            opts: Dict = None,
    ) -> models.ModifyNatGatewayAttributeResponse:
        """
        This API is used to modify the attributes of a NAT gateway.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyNatGatewayAttribute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyNatGatewayAttributeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyNatGatewayDestinationIpPortTranslationNatRule(
            self,
            request: models.ModifyNatGatewayDestinationIpPortTranslationNatRuleRequest,
            opts: Dict = None,
    ) -> models.ModifyNatGatewayDestinationIpPortTranslationNatRuleResponse:
        """
        This API is used to modify the port forwarding rule of a NAT gateway.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyNatGatewayDestinationIpPortTranslationNatRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyNatGatewayDestinationIpPortTranslationNatRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyNatGatewaySourceIpTranslationNatRule(
            self,
            request: models.ModifyNatGatewaySourceIpTranslationNatRuleRequest,
            opts: Dict = None,
    ) -> models.ModifyNatGatewaySourceIpTranslationNatRuleResponse:
        """
        This API is used to modify a NAT gateway's SNAT forwarding rules.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyNatGatewaySourceIpTranslationNatRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyNatGatewaySourceIpTranslationNatRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyNetDetect(
            self,
            request: models.ModifyNetDetectRequest,
            opts: Dict = None,
    ) -> models.ModifyNetDetectResponse:
        """
        This API (ModifyNetDetect) is used to modify network detection parameters.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyNetDetect"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyNetDetectResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyNetworkAclAttribute(
            self,
            request: models.ModifyNetworkAclAttributeRequest,
            opts: Dict = None,
    ) -> models.ModifyNetworkAclAttributeResponse:
        """
        This API is used to modify the attributes of a network ACL.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyNetworkAclAttribute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyNetworkAclAttributeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyNetworkAclEntries(
            self,
            request: models.ModifyNetworkAclEntriesRequest,
            opts: Dict = None,
    ) -> models.ModifyNetworkAclEntriesResponse:
        """
        This API is used to modify (add or delete) the inbound and outbound rules of a network ACL. In `NetworkAclEntrySet` parameters,
        * Passing in the new inbound/outbound rules will reset the original rules.
        * Passing in the inbound rules will only reset the original inbound rules and not affect the original outbound rules, and vice versa.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyNetworkAclEntries"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyNetworkAclEntriesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyNetworkAclQuintupleEntries(
            self,
            request: models.ModifyNetworkAclQuintupleEntriesRequest,
            opts: Dict = None,
    ) -> models.ModifyNetworkAclQuintupleEntriesResponse:
        """
        This API is used to modify the in/outbound rules of the network ACL quintuple. In the `NetworkAclQuintupleEntrySet` parameters, `NetworkAclQuintupleEntryId` is required for `NetworkAclQuintupleEntry`.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyNetworkAclQuintupleEntries"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyNetworkAclQuintupleEntriesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyNetworkInterfaceAttribute(
            self,
            request: models.ModifyNetworkInterfaceAttributeRequest,
            opts: Dict = None,
    ) -> models.ModifyNetworkInterfaceAttributeResponse:
        """
        This API (ModifyNetworkInterfaceAttribute) is used to modify ENI attributes.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyNetworkInterfaceAttribute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyNetworkInterfaceAttributeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyPrivateIpAddressesAttribute(
            self,
            request: models.ModifyPrivateIpAddressesAttributeRequest,
            opts: Dict = None,
    ) -> models.ModifyPrivateIpAddressesAttributeResponse:
        """
        This API (ModifyPrivateIpAddressesAttribute) is used to modify the private IP attributes of an ENI.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyPrivateIpAddressesAttribute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyPrivateIpAddressesAttributeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyReserveIpAddress(
            self,
            request: models.ModifyReserveIpAddressRequest,
            opts: Dict = None,
    ) -> models.ModifyReserveIpAddressResponse:
        """
        This API is used to modify a reserved private IP address.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyReserveIpAddress"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyReserveIpAddressResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyRoutePolicyAttribute(
            self,
            request: models.ModifyRoutePolicyAttributeRequest,
            opts: Dict = None,
    ) -> models.ModifyRoutePolicyAttributeResponse:
        """
        This API is used to modify the route reception policy attribute.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyRoutePolicyAttribute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyRoutePolicyAttributeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyRouteTableAttribute(
            self,
            request: models.ModifyRouteTableAttributeRequest,
            opts: Dict = None,
    ) -> models.ModifyRouteTableAttributeResponse:
        """
        This API (ModifyRouteTableAttribute) is used to modify the attributes of a route table.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyRouteTableAttribute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyRouteTableAttributeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifySecurityGroupAttribute(
            self,
            request: models.ModifySecurityGroupAttributeRequest,
            opts: Dict = None,
    ) -> models.ModifySecurityGroupAttributeResponse:
        """
        This API (ModifySecurityGroupAttribute) is used to modify the attributes of a security group (SecurityGroupPolicy).
        """
        
        kwargs = {}
        kwargs["action"] = "ModifySecurityGroupAttribute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifySecurityGroupAttributeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifySecurityGroupPolicies(
            self,
            request: models.ModifySecurityGroupPoliciesRequest,
            opts: Dict = None,
    ) -> models.ModifySecurityGroupPoliciesResponse:
        """
        This API is used to reset the `Egress` and `Ingress` rules (SecurityGroupPolicy) of a security group.

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
        """
        
        kwargs = {}
        kwargs["action"] = "ModifySecurityGroupPolicies"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifySecurityGroupPoliciesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyServiceTemplateAttribute(
            self,
            request: models.ModifyServiceTemplateAttributeRequest,
            opts: Dict = None,
    ) -> models.ModifyServiceTemplateAttributeResponse:
        """
        This API (ModifyServiceTemplateAttribute) is used to modify a protocol port template.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyServiceTemplateAttribute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyServiceTemplateAttributeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyServiceTemplateGroupAttribute(
            self,
            request: models.ModifyServiceTemplateGroupAttributeRequest,
            opts: Dict = None,
    ) -> models.ModifyServiceTemplateGroupAttributeResponse:
        """
        This API (ModifyServiceTemplateGroupAttribute) is used to modify a protocol port template group.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyServiceTemplateGroupAttribute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyServiceTemplateGroupAttributeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifySnapshotPolicies(
            self,
            request: models.ModifySnapshotPoliciesRequest,
            opts: Dict = None,
    ) -> models.ModifySnapshotPoliciesResponse:
        """
        This API is used to modify specified snapshot policies.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifySnapshotPolicies"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifySnapshotPoliciesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifySubnetAttribute(
            self,
            request: models.ModifySubnetAttributeRequest,
            opts: Dict = None,
    ) -> models.ModifySubnetAttributeResponse:
        """
        This API (ModifySubnetAttribute) is used to modify subnet attributes.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifySubnetAttribute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifySubnetAttributeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyTemplateMember(
            self,
            request: models.ModifyTemplateMemberRequest,
            opts: Dict = None,
    ) -> models.ModifyTemplateMemberResponse:
        """
        This API is used to modify a parameter template of the IP address, protocol port, IP address group, or protocol port group type.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyTemplateMember"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyTemplateMemberResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyVpcAttribute(
            self,
            request: models.ModifyVpcAttributeRequest,
            opts: Dict = None,
    ) -> models.ModifyVpcAttributeResponse:
        """
        This API (ModifyVpcAttribute) is used to modify VPC attributes.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyVpcAttribute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyVpcAttributeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyVpcEndPointAttribute(
            self,
            request: models.ModifyVpcEndPointAttributeRequest,
            opts: Dict = None,
    ) -> models.ModifyVpcEndPointAttributeResponse:
        """
        This API is used to modify endpoint attributes.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyVpcEndPointAttribute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyVpcEndPointAttributeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyVpcEndPointServiceAttribute(
            self,
            request: models.ModifyVpcEndPointServiceAttributeRequest,
            opts: Dict = None,
    ) -> models.ModifyVpcEndPointServiceAttributeResponse:
        """
        This API is used to modify the VPC endpoint service attributes.

        """
        
        kwargs = {}
        kwargs["action"] = "ModifyVpcEndPointServiceAttribute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyVpcEndPointServiceAttributeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyVpcEndPointServiceWhiteList(
            self,
            request: models.ModifyVpcEndPointServiceWhiteListRequest,
            opts: Dict = None,
    ) -> models.ModifyVpcEndPointServiceWhiteListResponse:
        """
        This API is used to modify the attributes of the endpoint service allowlist.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyVpcEndPointServiceWhiteList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyVpcEndPointServiceWhiteListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyVpnConnectionAttribute(
            self,
            request: models.ModifyVpnConnectionAttributeRequest,
            opts: Dict = None,
    ) -> models.ModifyVpnConnectionAttributeResponse:
        """
        This API (ModifyVpnConnectionAttribute) is used to modify VPN tunnels.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyVpnConnectionAttribute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyVpnConnectionAttributeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyVpnGatewayAttribute(
            self,
            request: models.ModifyVpnGatewayAttributeRequest,
            opts: Dict = None,
    ) -> models.ModifyVpnGatewayAttributeResponse:
        """
        This API (ModifyVpnGatewayAttribute) is used to modify the attributes of VPN gateways.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyVpnGatewayAttribute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyVpnGatewayAttributeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyVpnGatewayCcnRoutes(
            self,
            request: models.ModifyVpnGatewayCcnRoutesRequest,
            opts: Dict = None,
    ) -> models.ModifyVpnGatewayCcnRoutesResponse:
        """
        This API is used to modify VPN gateway-based CCN routes.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyVpnGatewayCcnRoutes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyVpnGatewayCcnRoutesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyVpnGatewayRoutes(
            self,
            request: models.ModifyVpnGatewayRoutesRequest,
            opts: Dict = None,
    ) -> models.ModifyVpnGatewayRoutesResponse:
        """
        This API is used to modify VPN gateway routes.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyVpnGatewayRoutes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyVpnGatewayRoutesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def NotifyRoutes(
            self,
            request: models.NotifyRoutesRequest,
            opts: Dict = None,
    ) -> models.NotifyRoutesResponse:
        """
        This API is used to publish a route to CCN. This can also be done by clicking "Publish to CCN" in the operation column on the page of route table list.
        """
        
        kwargs = {}
        kwargs["action"] = "NotifyRoutes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.NotifyRoutesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RefreshDirectConnectGatewayRouteToNatGateway(
            self,
            request: models.RefreshDirectConnectGatewayRouteToNatGatewayRequest,
            opts: Dict = None,
    ) -> models.RefreshDirectConnectGatewayRouteToNatGatewayResponse:
        """
        This API is used to refresh the route between a NAT gateway and  Direct Connect and update the associated route table.
        """
        
        kwargs = {}
        kwargs["action"] = "RefreshDirectConnectGatewayRouteToNatGateway"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RefreshDirectConnectGatewayRouteToNatGatewayResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RejectAttachCcnInstances(
            self,
            request: models.RejectAttachCcnInstancesRequest,
            opts: Dict = None,
    ) -> models.RejectAttachCcnInstancesResponse:
        """
        This API (RejectAttachCcnInstances) is used to reject association operations when instances are associated across accounts for the CCN owner.
        """
        
        kwargs = {}
        kwargs["action"] = "RejectAttachCcnInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RejectAttachCcnInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ReleaseAddresses(
            self,
            request: models.ReleaseAddressesRequest,
            opts: Dict = None,
    ) -> models.ReleaseAddressesResponse:
        """
        This API (ReleaseAddresses) is used to release one or multiple [Elastic IPs](https://intl.cloud.tencent.com/document/product/213/1941?from_cn_redirect=1).
        * This operation is irreversible. Once you release an EIP, the IP address associated with the EIP no longer belongs to you.
        * Only EIPs in UNBIND status can be released.
        """
        
        kwargs = {}
        kwargs["action"] = "ReleaseAddresses"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ReleaseAddressesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ReleaseIPv6Addresses(
            self,
            request: models.ReleaseIPv6AddressesRequest,
            opts: Dict = None,
    ) -> models.ReleaseIPv6AddressesResponse:
        """
        This API is used to release one or more EIPv6 instances.

        - You can release the obtained EIPv6 instances. To use them again, please reapply.
        - Only EIPv6 instances in UNBIND status can be released.
        """
        
        kwargs = {}
        kwargs["action"] = "ReleaseIPv6Addresses"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ReleaseIPv6AddressesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ReleaseIp6AddressesBandwidth(
            self,
            request: models.ReleaseIp6AddressesBandwidthRequest,
            opts: Dict = None,
    ) -> models.ReleaseIp6AddressesBandwidthResponse:
        """
        This API is used to release the IPv6 public network bandwidth of classic elastic public IPv6 instances.

        - Classic elastic public IPv6 addresses still have the IPv6 private network communication capability after the public network bandwidth is released.
        - To allocate IPV6 public network bandwidth, call the AllocateIp6AddressesBandwidth API.
        """
        
        kwargs = {}
        kwargs["action"] = "ReleaseIp6AddressesBandwidth"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ReleaseIp6AddressesBandwidthResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RemoveBandwidthPackageResources(
            self,
            request: models.RemoveBandwidthPackageResourcesRequest,
            opts: Dict = None,
    ) -> models.RemoveBandwidthPackageResourcesResponse:
        """
        This API is used to delete a bandwidth package resource, including [Elastic IP](https://intl.cloud.tencent.com/document/product/213/1941?from_cn_redirect=1), [Cloud Load Balancer](https://intl.cloud.tencent.com/document/product/214/517?from_cn_redirect=1), and so on.
        """
        
        kwargs = {}
        kwargs["action"] = "RemoveBandwidthPackageResources"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RemoveBandwidthPackageResourcesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RenewVpnGateway(
            self,
            request: models.RenewVpnGatewayRequest,
            opts: Dict = None,
    ) -> models.RenewVpnGatewayResponse:
        """
        This API (RenewVpnGateway) is used to renew prepaid (monthly subscription) VPN gateways. Currently, only IPSEC gateways are supported.
        """
        
        kwargs = {}
        kwargs["action"] = "RenewVpnGateway"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RenewVpnGatewayResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ReplaceDirectConnectGatewayCcnRoutes(
            self,
            request: models.ReplaceDirectConnectGatewayCcnRoutesRequest,
            opts: Dict = None,
    ) -> models.ReplaceDirectConnectGatewayCcnRoutesResponse:
        """
        This API (ReplaceDirectConnectGatewayCcnRoutes) is used to modify the specified route according to the route ID. Batch modification is supported.
        """
        
        kwargs = {}
        kwargs["action"] = "ReplaceDirectConnectGatewayCcnRoutes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ReplaceDirectConnectGatewayCcnRoutesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ReplaceRoutePolicyAssociations(
            self,
            request: models.ReplaceRoutePolicyAssociationsRequest,
            opts: Dict = None,
    ) -> models.ReplaceRoutePolicyAssociationsResponse:
        """
        This API is used to modify the binding Priority (Priority) based on the route reception policy instance ID (RoutePolicyId) and route table instance ID (RouteTableId), supporting batch modification.
        """
        
        kwargs = {}
        kwargs["action"] = "ReplaceRoutePolicyAssociations"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ReplaceRoutePolicyAssociationsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ReplaceRoutePolicyEntries(
            self,
            request: models.ReplaceRoutePolicyEntriesRequest,
            opts: Dict = None,
    ) -> models.ReplaceRoutePolicyEntriesResponse:
        """
        This API is used to modify specified routing policy entries based on route reception policy rule ID and supports batch modification.
        """
        
        kwargs = {}
        kwargs["action"] = "ReplaceRoutePolicyEntries"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ReplaceRoutePolicyEntriesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ReplaceRouteTableAssociation(
            self,
            request: models.ReplaceRouteTableAssociationRequest,
            opts: Dict = None,
    ) -> models.ReplaceRouteTableAssociationResponse:
        """
        This API (ReplaceRouteTableAssociation) is used to modify the route table associated with a subnet.
        * A subnet can only be associated with one route table.
        """
        
        kwargs = {}
        kwargs["action"] = "ReplaceRouteTableAssociation"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ReplaceRouteTableAssociationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ReplaceRoutes(
            self,
            request: models.ReplaceRoutesRequest,
            opts: Dict = None,
    ) -> models.ReplaceRoutesResponse:
        """
        This API (ReplaceRoutes) is used to modify a specified routing policy by its ID (RouteId). Batch modification is supported.
        """
        
        kwargs = {}
        kwargs["action"] = "ReplaceRoutes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ReplaceRoutesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ReplaceSecurityGroupPolicies(
            self,
            request: models.ReplaceSecurityGroupPoliciesRequest,
            opts: Dict = None,
    ) -> models.ReplaceSecurityGroupPoliciesResponse:
        """
        This API is used to batch modify security group policies.
        Policies to modify must be in the same direction. `PolicyIndex` must be specified.
        """
        
        kwargs = {}
        kwargs["action"] = "ReplaceSecurityGroupPolicies"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ReplaceSecurityGroupPoliciesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ReplaceSecurityGroupPolicy(
            self,
            request: models.ReplaceSecurityGroupPolicyRequest,
            opts: Dict = None,
    ) -> models.ReplaceSecurityGroupPolicyResponse:
        """
        This API (ReplaceSecurityGroupPolicy) is used to replace a single security group policy (SecurityGroupPolicy).
        Only one policy in a single direction can be replaced in each request, and the PolicyIndex parameter must be specified.
        """
        
        kwargs = {}
        kwargs["action"] = "ReplaceSecurityGroupPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ReplaceSecurityGroupPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ResetAttachCcnInstances(
            self,
            request: models.ResetAttachCcnInstancesRequest,
            opts: Dict = None,
    ) -> models.ResetAttachCcnInstancesResponse:
        """
        This API (ResetAttachCcnInstances) is used to re-apply for the association operation when the application for cross-account instance association expires.
        """
        
        kwargs = {}
        kwargs["action"] = "ResetAttachCcnInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ResetAttachCcnInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ResetNatGatewayConnection(
            self,
            request: models.ResetNatGatewayConnectionRequest,
            opts: Dict = None,
    ) -> models.ResetNatGatewayConnectionResponse:
        """
        This API is used to adjust concurrent connection cap for the NAT gateway.
        """
        
        kwargs = {}
        kwargs["action"] = "ResetNatGatewayConnection"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ResetNatGatewayConnectionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ResetRoutePolicyAssociations(
            self,
            request: models.ResetRoutePolicyAssociationsRequest,
            opts: Dict = None,
    ) -> models.ResetRoutePolicyAssociationsResponse:
        """
        This API is used to unbind the routing policy instance already bound to a specific route table instance, set up alarms for the new binding routing policy and priority.
        """
        
        kwargs = {}
        kwargs["action"] = "ResetRoutePolicyAssociations"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ResetRoutePolicyAssociationsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ResetRoutePolicyEntries(
            self,
            request: models.ResetRoutePolicyEntriesRequest,
            opts: Dict = None,
    ) -> models.ResetRoutePolicyEntriesResponse:
        """
        This API is used to reset the designated route reception policy entry based on the rule ID and supports batch modification.
        """
        
        kwargs = {}
        kwargs["action"] = "ResetRoutePolicyEntries"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ResetRoutePolicyEntriesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ResetRoutes(
            self,
            request: models.ResetRoutesRequest,
            opts: Dict = None,
    ) -> models.ResetRoutesResponse:
        """
        This API (ResetRoutes) is used to reset the name of a route table and all its routing policies.<br />
        Note: When this API is called, all routing policies in the current route table are deleted before new routing policies are saved, which may incur network interruption.
        """
        
        kwargs = {}
        kwargs["action"] = "ResetRoutes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ResetRoutesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ResetVpnConnection(
            self,
            request: models.ResetVpnConnectionRequest,
            opts: Dict = None,
    ) -> models.ResetVpnConnectionResponse:
        """
        The API is used to reset a VPN tunnel.
        """
        
        kwargs = {}
        kwargs["action"] = "ResetVpnConnection"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ResetVpnConnectionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ResetVpnGatewayInternetMaxBandwidth(
            self,
            request: models.ResetVpnGatewayInternetMaxBandwidthRequest,
            opts: Dict = None,
    ) -> models.ResetVpnGatewayInternetMaxBandwidthResponse:
        """
        This API is used to adjust the bandwidth cap of a VPN gateway. The adjustment of the VPN gateway bandwidth is limited to [5,100] Mbps and [200,1000] Mbps.
        """
        
        kwargs = {}
        kwargs["action"] = "ResetVpnGatewayInternetMaxBandwidth"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ResetVpnGatewayInternetMaxBandwidthResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ResumeSnapshotInstance(
            self,
            request: models.ResumeSnapshotInstanceRequest,
            opts: Dict = None,
    ) -> models.ResumeSnapshotInstanceResponse:
        """
        This API is used to restore security group policies with a backup.
        """
        
        kwargs = {}
        kwargs["action"] = "ResumeSnapshotInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ResumeSnapshotInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ReturnNormalAddresses(
            self,
            request: models.ReturnNormalAddressesRequest,
            opts: Dict = None,
    ) -> models.ReturnNormalAddressesResponse:
        """
        This API is used to unbind and release public IPs.
        Note: Starting from Dec 15, 2022, CAM authorization is required for a sub-account to call this API. For more details, see [Authorization Guide](https://intl.cloud.tencent.com/document/product/598/34545?from_cn_redirect=1).
        """
        
        kwargs = {}
        kwargs["action"] = "ReturnNormalAddresses"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ReturnNormalAddressesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SetCcnRegionBandwidthLimits(
            self,
            request: models.SetCcnRegionBandwidthLimitsRequest,
            opts: Dict = None,
    ) -> models.SetCcnRegionBandwidthLimitsResponse:
        """
        This API (SetCcnRegionBandwidthLimits) is used to set the outbound bandwidth cap for CCNs in each region. This API can only set the outbound bandwidth cap for regions in the network instances that have already been associated.
        """
        
        kwargs = {}
        kwargs["action"] = "SetCcnRegionBandwidthLimits"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SetCcnRegionBandwidthLimitsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SetVpnGatewaysRenewFlag(
            self,
            request: models.SetVpnGatewaysRenewFlagRequest,
            opts: Dict = None,
    ) -> models.SetVpnGatewaysRenewFlagResponse:
        """
        This API is used set the auto-renewal configuration of a VPN gateway.
        """
        
        kwargs = {}
        kwargs["action"] = "SetVpnGatewaysRenewFlag"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SetVpnGatewaysRenewFlagResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def TransformAddress(
            self,
            request: models.TransformAddressRequest,
            opts: Dict = None,
    ) -> models.TransformAddressResponse:
        """
        This API is used to convert a common public IP into an [Elastic IP](https://intl.cloud.tencent.com/document/product/213/1941?from_cn_redirect=1) (EIP for short).
        * Tencent Cloud limits the number of times that a user can unbind EIPs and reassign public IPs in each region per day. For more information, see product introduction of [Elastic IP](https://intl.cloud.tencent.com/document/product/213/5733?from_cn_redirect=1). The preceding quota can be obtained through the API [DescribeAddressQuota](https://intl.cloud.tencent.com/document/product/215/16701).
        """
        
        kwargs = {}
        kwargs["action"] = "TransformAddress"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.TransformAddressResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UnassignIpv6Addresses(
            self,
            request: models.UnassignIpv6AddressesRequest,
            opts: Dict = None,
    ) -> models.UnassignIpv6AddressesResponse:
        """
        This API is used to release the IPv6 addresses of an ENI. <br />
        This API is completed asynchronously. If you need to query the execution result of an async task, please use the `RequestId` returned by this API to poll the `DescribeVpcTaskResult` API.
        """
        
        kwargs = {}
        kwargs["action"] = "UnassignIpv6Addresses"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UnassignIpv6AddressesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UnassignIpv6CidrBlock(
            self,
            request: models.UnassignIpv6CidrBlockRequest,
            opts: Dict = None,
    ) -> models.UnassignIpv6CidrBlockResponse:
        """
        This API (UnassignIpv6CidrBlock) is used to release IPv6 IP ranges.
        If the IP range still has occupied IPs that are not yet repossessed, the IP range cannot be released.
        """
        
        kwargs = {}
        kwargs["action"] = "UnassignIpv6CidrBlock"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UnassignIpv6CidrBlockResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UnassignIpv6SubnetCidrBlock(
            self,
            request: models.UnassignIpv6SubnetCidrBlockRequest,
            opts: Dict = None,
    ) -> models.UnassignIpv6SubnetCidrBlockResponse:
        """
        This API (UnassignIpv6SubnetCidrBlock) is used to release IPv6 subnet IP ranges.
        If the subnet IP range still has occupied IPs that are not yet repossessed, the subnet IP range cannot be released.
        """
        
        kwargs = {}
        kwargs["action"] = "UnassignIpv6SubnetCidrBlock"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UnassignIpv6SubnetCidrBlockResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UnassignPrivateIpAddresses(
            self,
            request: models.UnassignPrivateIpAddressesRequest,
            opts: Dict = None,
    ) -> models.UnassignPrivateIpAddressesResponse:
        """
        This API is used to return the private IP addresses of an ENI.
        * If a secondary private IP of an ENI is returned, the EIP will be automatically unassociated as well. The primary private IP of the ENI cannot be returned.

        This API is completed asynchronously. If you need to query the execution result of an async task, please use the `RequestId` returned by this API to poll the `DescribeVpcTaskResult` API.
        """
        
        kwargs = {}
        kwargs["action"] = "UnassignPrivateIpAddresses"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UnassignPrivateIpAddressesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def WithdrawNotifyRoutes(
            self,
            request: models.WithdrawNotifyRoutesRequest,
            opts: Dict = None,
    ) -> models.WithdrawNotifyRoutesResponse:
        """
        This API is used to withdraw a route from CCN.
        """
        
        kwargs = {}
        kwargs["action"] = "WithdrawNotifyRoutes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.WithdrawNotifyRoutesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)