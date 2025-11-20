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
from tencentcloud.ecm.v20190719 import models
from typing import Dict


class EcmClient(AbstractClient):
    _apiVersion = '2019-07-19'
    _endpoint = 'ecm.intl.tencentcloudapi.com'
    _service = 'ecm'

    async def AllocateAddresses(
            self,
            request: models.AllocateAddressesRequest,
            opts: Dict = None,
    ) -> models.AllocateAddressesResponse:
        """
        This API is used to apply for one or multiple EIPs.
        """
        
        kwargs = {}
        kwargs["action"] = "AllocateAddresses"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AllocateAddressesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AssignIpv6Addresses(
            self,
            request: models.AssignIpv6AddressesRequest,
            opts: Dict = None,
    ) -> models.AssignIpv6AddressesResponse:
        """
        This API is used to apply for an IPv6 address for an ENI.
        """
        
        kwargs = {}
        kwargs["action"] = "AssignIpv6Addresses"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AssignIpv6AddressesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AssignPrivateIpAddresses(
            self,
            request: models.AssignPrivateIpAddressesRequest,
            opts: Dict = None,
    ) -> models.AssignPrivateIpAddressesResponse:
        """
        This API is used to apply for a private IP for an ENI.
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
        This API is used to bind an EIP to an instance or the specified private IP of an ENI.
        Binding an EIP to an instance (ECM) is essentially to bind it to the primary private IP of the primary ENI of the instance.
        When you bind an EIP to the private IP of the specified ENI, if the private IP is already bound to an EIP or public IP, a failure will be reported, and you must unbind it first before you can bind it to a new EIP.
        Only EIPs in `UNBIND` status can be bound to a private IP.
        """
        
        kwargs = {}
        kwargs["action"] = "AssociateAddress"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AssociateAddressResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AssociateSecurityGroups(
            self,
            request: models.AssociateSecurityGroupsRequest,
            opts: Dict = None,
    ) -> models.AssociateSecurityGroupsResponse:
        """
        This API is used to bind a security group.
        """
        
        kwargs = {}
        kwargs["action"] = "AssociateSecurityGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AssociateSecurityGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AttachNetworkInterface(
            self,
            request: models.AttachNetworkInterfaceRequest,
            opts: Dict = None,
    ) -> models.AttachNetworkInterfaceResponse:
        """
        This API is used to bind an ENI to a CVM instance.
        """
        
        kwargs = {}
        kwargs["action"] = "AttachNetworkInterface"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AttachNetworkInterfaceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BatchDeregisterTargets(
            self,
            request: models.BatchDeregisterTargetsRequest,
            opts: Dict = None,
    ) -> models.BatchDeregisterTargetsResponse:
        """
        This API is used to batch unbind real servers.
        """
        
        kwargs = {}
        kwargs["action"] = "BatchDeregisterTargets"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BatchDeregisterTargetsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BatchModifyTargetWeight(
            self,
            request: models.BatchModifyTargetWeightRequest,
            opts: Dict = None,
    ) -> models.BatchModifyTargetWeightResponse:
        """
        This API is used to batch modify the forwarding weights of the real servers bound to a listener.
        """
        
        kwargs = {}
        kwargs["action"] = "BatchModifyTargetWeight"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BatchModifyTargetWeightResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BatchRegisterTargets(
            self,
            request: models.BatchRegisterTargetsRequest,
            opts: Dict = None,
    ) -> models.BatchRegisterTargetsResponse:
        """
        This API is used to batch bind backend targets.
        """
        
        kwargs = {}
        kwargs["action"] = "BatchRegisterTargets"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BatchRegisterTargetsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateHaVip(
            self,
            request: models.CreateHaVipRequest,
            opts: Dict = None,
    ) -> models.CreateHaVipResponse:
        """
        This API is used to create an HAVIP.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateHaVip"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateHaVipResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateImage(
            self,
            request: models.CreateImageRequest,
            opts: Dict = None,
    ) -> models.CreateImageResponse:
        """
        This API is used to create an image with the system disk of an instance. The image can be used to create instances.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateImage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateImageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateKeyPair(
            self,
            request: models.CreateKeyPairRequest,
            opts: Dict = None,
    ) -> models.CreateKeyPairResponse:
        """
        This API is used to create an `OpenSSH RSA` key pair, which can be used to log in to a Linux instance.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateKeyPair"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateKeyPairResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateListener(
            self,
            request: models.CreateListenerRequest,
            opts: Dict = None,
    ) -> models.CreateListenerResponse:
        """
        This API is used to create a CLB listener.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateListener"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateListenerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateLoadBalancer(
            self,
            request: models.CreateLoadBalancerRequest,
            opts: Dict = None,
    ) -> models.CreateLoadBalancerResponse:
        """
        This API is used to purchase a CLB instance.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateLoadBalancer"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateLoadBalancerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateModule(
            self,
            request: models.CreateModuleRequest,
            opts: Dict = None,
    ) -> models.CreateModuleResponse:
        """
        This API is used to create a module.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateModule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateModuleResponse
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
        """
        
        kwargs = {}
        kwargs["action"] = "CreateNetworkInterface"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateNetworkInterfaceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateRouteTable(
            self,
            request: models.CreateRouteTableRequest,
            opts: Dict = None,
    ) -> models.CreateRouteTableResponse:
        """
        After a VPC is created, the system will create a default route table, with which all new subnets will be associated. By default, you can use the default route table to manage your routing policies. If you have multiple routing policies, you can call the API for route table creation to create more route tables to manage your routing policies.
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
        This API is used to create a routing policy.
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
        This API is used to create a security group.
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
        <p>This API is used to create a security group policy.</p>
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
        """
        
        kwargs = {}
        kwargs["action"] = "CreateSecurityGroupPolicies"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateSecurityGroupPoliciesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateSubnet(
            self,
            request: models.CreateSubnetRequest,
            opts: Dict = None,
    ) -> models.CreateSubnetResponse:
        """
        This API is used to create a subnet. After the subnet is created successfully, it will become the default subnet for the AZ.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateSubnet"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateSubnetResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateVpc(
            self,
            request: models.CreateVpcRequest,
            opts: Dict = None,
    ) -> models.CreateVpcResponse:
        """
        This API is used to create a VPC.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateVpc"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateVpcResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteHaVip(
            self,
            request: models.DeleteHaVipRequest,
            opts: Dict = None,
    ) -> models.DeleteHaVipResponse:
        """
        This API is used to delete an HAVIP.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteHaVip"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteHaVipResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteImage(
            self,
            request: models.DeleteImageRequest,
            opts: Dict = None,
    ) -> models.DeleteImageResponse:
        """
        This API is used to delete an image.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteImage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteImageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteListener(
            self,
            request: models.DeleteListenerRequest,
            opts: Dict = None,
    ) -> models.DeleteListenerResponse:
        """
        This API is used to delete a CLB listener.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteListener"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteListenerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteLoadBalancer(
            self,
            request: models.DeleteLoadBalancerRequest,
            opts: Dict = None,
    ) -> models.DeleteLoadBalancerResponse:
        """
        This API is used to delete a CLB instance.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteLoadBalancer"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteLoadBalancerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteLoadBalancerListeners(
            self,
            request: models.DeleteLoadBalancerListenersRequest,
            opts: Dict = None,
    ) -> models.DeleteLoadBalancerListenersResponse:
        """
        This API is used to delete multiple CLB listeners.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteLoadBalancerListeners"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteLoadBalancerListenersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteModule(
            self,
            request: models.DeleteModuleRequest,
            opts: Dict = None,
    ) -> models.DeleteModuleResponse:
        """
        This API is used to delete a business module.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteModule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteModuleResponse
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
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteNetworkInterface"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteNetworkInterfaceResponse
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
        This API is used to batch delete routing policies from a route table.
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
        Only security groups under the current account can be deleted.
        A security group cannot be deleted directly if its instance ID is used in the policy of another security group. In this case, you need to modify the policy first before deleting the security group.
        Deleted security groups cannot be recovered. Therefore, call this API with caution.
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
        `SecurityGroupPolicySet.Version` is used to specify the version of the security group to be manipulated. If the `Version` value passed in differs from the current latest version of the security group, a failure will be returned. If `Version` is not passed in, the policy of the specified `PolicyIndex` will be deleted directly.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteSecurityGroupPolicies"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteSecurityGroupPoliciesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteSnapshots(
            self,
            request: models.DeleteSnapshotsRequest,
            opts: Dict = None,
    ) -> models.DeleteSnapshotsResponse:
        """
        This API is used to delete a snapshot.

        * Only snapshots in the `NORMAL` state can be deleted. To query the state of a snapshot, you can call the [DescribeSnapshots](https://intl.cloud.tencent.com/document/product/362/15647?from_cn_redirect=1) API and check the `SnapshotState` field in the response.
        * Batch operations are supported. If there is any snapshot that cannot be deleted, the operation will not be performed and a specific error code will be returned.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteSnapshots"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteSnapshotsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteSubnet(
            self,
            request: models.DeleteSubnetRequest,
            opts: Dict = None,
    ) -> models.DeleteSubnetResponse:
        """
        This API is used to delete a subnet. If the subnet is the current default subnet in the AZ, after it is deleted, the default subnet automatically created by the system rather than the last subnet created by you will be used as the new default subnet. If the new default subnet does not meet your needs, you can call the API for setting the default subnet to configure it.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteSubnet"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteSubnetResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteVpc(
            self,
            request: models.DeleteVpcRequest,
            opts: Dict = None,
    ) -> models.DeleteVpcResponse:
        """
        This API is used to delete a VPC.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteVpc"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteVpcResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAddressQuota(
            self,
            request: models.DescribeAddressQuotaRequest,
            opts: Dict = None,
    ) -> models.DescribeAddressQuotaResponse:
        """
        This API is used to query the quota information of the EIP under your account in the current region.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAddressQuota"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAddressQuotaResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAddresses(
            self,
            request: models.DescribeAddressesRequest,
            opts: Dict = None,
    ) -> models.DescribeAddressesResponse:
        """
        This API is used to query the list of EIPs.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAddresses"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAddressesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBaseOverview(
            self,
            request: models.DescribeBaseOverviewRequest,
            opts: Dict = None,
    ) -> models.DescribeBaseOverviewResponse:
        """
        This API is used to get the basic data displayed on the overview page.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBaseOverview"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBaseOverviewResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeConfig(
            self,
            request: models.DescribeConfigRequest,
            opts: Dict = None,
    ) -> models.DescribeConfigResponse:
        """
        This API is used to get the limits of data such as bandwidth and disk.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCustomImageTask(
            self,
            request: models.DescribeCustomImageTaskRequest,
            opts: Dict = None,
    ) -> models.DescribeCustomImageTaskResponse:
        """
        This API is used to query an image import task.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCustomImageTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCustomImageTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDefaultSubnet(
            self,
            request: models.DescribeDefaultSubnetRequest,
            opts: Dict = None,
    ) -> models.DescribeDefaultSubnetResponse:
        """
        This API is used to query the default subnet in an AZ.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDefaultSubnet"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDefaultSubnetResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeHaVips(
            self,
            request: models.DescribeHaVipsRequest,
            opts: Dict = None,
    ) -> models.DescribeHaVipsResponse:
        """
        This API is used to query the list of HAVIPs.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeHaVips"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeHaVipsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeImage(
            self,
            request: models.DescribeImageRequest,
            opts: Dict = None,
    ) -> models.DescribeImageResponse:
        """
        This API is used to display the list of images.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeImage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeImageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeImportImageOs(
            self,
            request: models.DescribeImportImageOsRequest,
            opts: Dict = None,
    ) -> models.DescribeImportImageOsResponse:
        """
        This API is used to query the list of operating systems supported by an image imported from an external resource.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeImportImageOs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeImportImageOsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstanceTypeConfig(
            self,
            request: models.DescribeInstanceTypeConfigRequest,
            opts: Dict = None,
    ) -> models.DescribeInstanceTypeConfigResponse:
        """
        This API is used to get the list of model configurations.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstanceTypeConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstanceTypeConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstanceVncUrl(
            self,
            request: models.DescribeInstanceVncUrlRequest,
            opts: Dict = None,
    ) -> models.DescribeInstanceVncUrlResponse:
        """
        This API is used to query the VNC URL of an instance.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstanceVncUrl"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstanceVncUrlResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstances(
            self,
            request: models.DescribeInstancesRequest,
            opts: Dict = None,
    ) -> models.DescribeInstancesResponse:
        """
        This API is used to get the information of an instance.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstancesDeniedActions(
            self,
            request: models.DescribeInstancesDeniedActionsRequest,
            opts: Dict = None,
    ) -> models.DescribeInstancesDeniedActionsResponse:
        """
        This API is used to get the information of prohibited operations by instance ID.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstancesDeniedActions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstancesDeniedActionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeListeners(
            self,
            request: models.DescribeListenersRequest,
            opts: Dict = None,
    ) -> models.DescribeListenersResponse:
        """
        This API is used to query the list of CLB listeners.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeListeners"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeListenersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLoadBalanceTaskStatus(
            self,
            request: models.DescribeLoadBalanceTaskStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeLoadBalanceTaskStatusResponse:
        """
        This API is used to query the task status of a CLB instance.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLoadBalanceTaskStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLoadBalanceTaskStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLoadBalancers(
            self,
            request: models.DescribeLoadBalancersRequest,
            opts: Dict = None,
    ) -> models.DescribeLoadBalancersResponse:
        """
        This API is used to query the list of CLB instances.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLoadBalancers"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLoadBalancersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeModule(
            self,
            request: models.DescribeModuleRequest,
            opts: Dict = None,
    ) -> models.DescribeModuleResponse:
        """
        This API is used to get the list of modules.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeModule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeModuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeModuleDetail(
            self,
            request: models.DescribeModuleDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeModuleDetailResponse:
        """
        This API is used to display the details of a module.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeModuleDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeModuleDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMonthPeakNetwork(
            self,
            request: models.DescribeMonthPeakNetworkRequest,
            opts: Dict = None,
    ) -> models.DescribeMonthPeakNetworkResponse:
        """
        This API is used to get the monthly peak and billable inbound/outbound bandwidth values of your node.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMonthPeakNetwork"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMonthPeakNetworkResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeNetworkInterfaces(
            self,
            request: models.DescribeNetworkInterfacesRequest,
            opts: Dict = None,
    ) -> models.DescribeNetworkInterfacesResponse:
        """
        This API is used to query the list of ENIs.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeNetworkInterfaces"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeNetworkInterfacesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeNode(
            self,
            request: models.DescribeNodeRequest,
            opts: Dict = None,
    ) -> models.DescribeNodeResponse:
        """
        This API is used to get the list of nodes.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeNode"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeNodeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePackingQuotaGroup(
            self,
            request: models.DescribePackingQuotaGroupRequest,
            opts: Dict = None,
    ) -> models.DescribePackingQuotaGroupResponse:
        """
        This API is used to get the packing quota of a model in a region (when a virtual model is used, a set of correlated packing quotas will be returned).
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePackingQuotaGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePackingQuotaGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePeakBaseOverview(
            self,
            request: models.DescribePeakBaseOverviewRequest,
            opts: Dict = None,
    ) -> models.DescribePeakBaseOverviewResponse:
        """
        This API is used to get the peak data of basic information such as CPU, memory, and disk.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePeakBaseOverview"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePeakBaseOverviewResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePeakNetworkOverview(
            self,
            request: models.DescribePeakNetworkOverviewRequest,
            opts: Dict = None,
    ) -> models.DescribePeakNetworkOverviewResponse:
        """
        This API is used to get the peak network data.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePeakNetworkOverview"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePeakNetworkOverviewResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePriceRunInstance(
            self,
            request: models.DescribePriceRunInstanceRequest,
            opts: Dict = None,
    ) -> models.DescribePriceRunInstanceResponse:
        """
        This API is used to query the price of an instance.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePriceRunInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePriceRunInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRouteConflicts(
            self,
            request: models.DescribeRouteConflictsRequest,
            opts: Dict = None,
    ) -> models.DescribeRouteConflictsResponse:
        """
        This API is used to query the list of conflicts between a custom routing policy and a CCN routing policy.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRouteConflicts"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRouteConflictsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRouteTables(
            self,
            request: models.DescribeRouteTablesRequest,
            opts: Dict = None,
    ) -> models.DescribeRouteTablesResponse:
        """
        This API is used to query the list of the objects in a route table.
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
        This API is used to query statistics on the instances associated with a security group.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSecurityGroupAssociationStatistics"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSecurityGroupAssociationStatisticsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSecurityGroupLimits(
            self,
            request: models.DescribeSecurityGroupLimitsRequest,
            opts: Dict = None,
    ) -> models.DescribeSecurityGroupLimitsResponse:
        """
        This API is used to query the security group quota.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSecurityGroupLimits"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSecurityGroupLimitsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSecurityGroupPolicies(
            self,
            request: models.DescribeSecurityGroupPoliciesRequest,
            opts: Dict = None,
    ) -> models.DescribeSecurityGroupPoliciesResponse:
        """
        This API is used to query a security group rule.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSecurityGroupPolicies"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSecurityGroupPoliciesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSecurityGroups(
            self,
            request: models.DescribeSecurityGroupsRequest,
            opts: Dict = None,
    ) -> models.DescribeSecurityGroupsResponse:
        """
        This API is used to view a security group.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSecurityGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSecurityGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSnapshots(
            self,
            request: models.DescribeSnapshotsRequest,
            opts: Dict = None,
    ) -> models.DescribeSnapshotsResponse:
        """
        This API is used to query the list of snapshots.

        * You can filter results by snapshot ID and the ID and type of the cloud disk for which the snapshot is created. The relationship between different filters is `AND`. For more information on filters, see `Filter`.
        * If no parameter is defined, the status of a certain number of snapshots under the current account will be returned. The number is specified by `Limit` and is 20 by default.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSnapshots"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSnapshotsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSubnets(
            self,
            request: models.DescribeSubnetsRequest,
            opts: Dict = None,
    ) -> models.DescribeSubnetsResponse:
        """
        This API is used to query the list of subnets.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSubnets"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSubnetsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTargetHealth(
            self,
            request: models.DescribeTargetHealthRequest,
            opts: Dict = None,
    ) -> models.DescribeTargetHealthResponse:
        """
        This API is used to get the health check status of a CLB real server.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTargetHealth"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTargetHealthResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTargets(
            self,
            request: models.DescribeTargetsRequest,
            opts: Dict = None,
    ) -> models.DescribeTargetsResponse:
        """
        This API is used to query the list of the real servers bound to a CLB instance.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTargets"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTargetsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTaskResult(
            self,
            request: models.DescribeTaskResultRequest,
            opts: Dict = None,
    ) -> models.DescribeTaskResultResponse:
        """
        This API is used to query the execution result of an EIP async task.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTaskResult"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTaskResultResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTaskStatus(
            self,
            request: models.DescribeTaskStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeTaskStatusResponse:
        """
        This API is used to get the status of an async task.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTaskStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTaskStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVpcs(
            self,
            request: models.DescribeVpcsRequest,
            opts: Dict = None,
    ) -> models.DescribeVpcsResponse:
        """
        This API is used to query the list of VPCs.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVpcs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVpcsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DetachNetworkInterface(
            self,
            request: models.DetachNetworkInterfaceRequest,
            opts: Dict = None,
    ) -> models.DetachNetworkInterfaceResponse:
        """
        This API is used to unbind an ENI from a CVM instance.
        """
        
        kwargs = {}
        kwargs["action"] = "DetachNetworkInterface"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DetachNetworkInterfaceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DisableRoutes(
            self,
            request: models.DisableRoutesRequest,
            opts: Dict = None,
    ) -> models.DisableRoutesResponse:
        """
        This API is used to disable a subnet route.
        """
        
        kwargs = {}
        kwargs["action"] = "DisableRoutes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DisableRoutesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DisassociateAddress(
            self,
            request: models.DisassociateAddressRequest,
            opts: Dict = None,
    ) -> models.DisassociateAddressResponse:
        """
        This API is used to unbind an EIP.
        Only EIPs in `BIND` or `BIND_ENI` status can be unbound.
        Blocked EIPs cannot be unbound.
        """
        
        kwargs = {}
        kwargs["action"] = "DisassociateAddress"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DisassociateAddressResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DisassociateInstancesKeyPairs(
            self,
            request: models.DisassociateInstancesKeyPairsRequest,
            opts: Dict = None,
    ) -> models.DisassociateInstancesKeyPairsResponse:
        """
        This API is used to unbind a key pair from an instance.
        """
        
        kwargs = {}
        kwargs["action"] = "DisassociateInstancesKeyPairs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DisassociateInstancesKeyPairsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DisassociateSecurityGroups(
            self,
            request: models.DisassociateSecurityGroupsRequest,
            opts: Dict = None,
    ) -> models.DisassociateSecurityGroupsResponse:
        """
        This API is used to unbind a security group.
        """
        
        kwargs = {}
        kwargs["action"] = "DisassociateSecurityGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DisassociateSecurityGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def EnableRoutes(
            self,
            request: models.EnableRoutesRequest,
            opts: Dict = None,
    ) -> models.EnableRoutesResponse:
        """
        This API is used to enable a disabled subnet route.
        This API verifies whether a CCN route will conflict with an existing route after it is enabled, and if so, you cannot enable it before you disable the conflicting route first.
        """
        
        kwargs = {}
        kwargs["action"] = "EnableRoutes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.EnableRoutesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ImportImage(
            self,
            request: models.ImportImageRequest,
            opts: Dict = None,
    ) -> models.ImportImageResponse:
        """
        This API is used to import an image from a CVM instance to an ECM instance.
        """
        
        kwargs = {}
        kwargs["action"] = "ImportImage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ImportImageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def MigrateNetworkInterface(
            self,
            request: models.MigrateNetworkInterfaceRequest,
            opts: Dict = None,
    ) -> models.MigrateNetworkInterfaceResponse:
        """
        This API is used to migrate an ENI.
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
        This API is used to migrate a private IP from an ENI.
        It migrates a private IP from one ENI to another. Primary IPs cannot be migrated.
        The source and destination ENIs must be in the same subnet.
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
        This API is used to modify EIP attributes.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAddressAttribute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAddressAttributeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAddressesBandwidth(
            self,
            request: models.ModifyAddressesBandwidthRequest,
            opts: Dict = None,
    ) -> models.ModifyAddressesBandwidthResponse:
        """
        This API is used to modify the EIP bandwidth.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAddressesBandwidth"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAddressesBandwidthResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDefaultSubnet(
            self,
            request: models.ModifyDefaultSubnetRequest,
            opts: Dict = None,
    ) -> models.ModifyDefaultSubnetResponse:
        """
        This API is used to modify the default subnet used when you create an instance in an AZ (if you don't specify the VPC parameter when creating the instance, `sunbetId` will be used).
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDefaultSubnet"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDefaultSubnetResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyHaVipAttribute(
            self,
            request: models.ModifyHaVipAttributeRequest,
            opts: Dict = None,
    ) -> models.ModifyHaVipAttributeResponse:
        """
        This API is used to modify the attributes of an HAVIP.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyHaVipAttribute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyHaVipAttributeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyImageAttribute(
            self,
            request: models.ModifyImageAttributeRequest,
            opts: Dict = None,
    ) -> models.ModifyImageAttributeResponse:
        """
        This API is used to modify the attributes of an image.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyImageAttribute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyImageAttributeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyInstancesAttribute(
            self,
            request: models.ModifyInstancesAttributeRequest,
            opts: Dict = None,
    ) -> models.ModifyInstancesAttributeResponse:
        """
        This API is used to modify the attributes of an instance.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyInstancesAttribute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyInstancesAttributeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyIpv6AddressesAttribute(
            self,
            request: models.ModifyIpv6AddressesAttributeRequest,
            opts: Dict = None,
    ) -> models.ModifyIpv6AddressesAttributeResponse:
        """
        This API is used to modify the IPv6 address attributes of an ENI.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyIpv6AddressesAttribute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyIpv6AddressesAttributeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyListener(
            self,
            request: models.ModifyListenerRequest,
            opts: Dict = None,
    ) -> models.ModifyListenerResponse:
        """
        This API is used to modify the attributes of a CLB listener.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyListener"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyListenerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyLoadBalancerAttributes(
            self,
            request: models.ModifyLoadBalancerAttributesRequest,
            opts: Dict = None,
    ) -> models.ModifyLoadBalancerAttributesResponse:
        """
        This API is used to modify the attributes of a CLB instance.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyLoadBalancerAttributes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyLoadBalancerAttributesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyModuleConfig(
            self,
            request: models.ModifyModuleConfigRequest,
            opts: Dict = None,
    ) -> models.ModifyModuleConfigResponse:
        """
        This API is used to modify the configuration of a module. You cannot modify the configuration of the module if it is associated with an instance.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyModuleConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyModuleConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyModuleDisableWanIp(
            self,
            request: models.ModifyModuleDisableWanIpRequest,
            opts: Dict = None,
    ) -> models.ModifyModuleDisableWanIpResponse:
        """
        This API is used to specify whether to prohibit public IP assignment for a module.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyModuleDisableWanIp"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyModuleDisableWanIpResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyModuleImage(
            self,
            request: models.ModifyModuleImageRequest,
            opts: Dict = None,
    ) -> models.ModifyModuleImageResponse:
        """
        This API is used to modify the default image of a module.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyModuleImage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyModuleImageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyModuleIpDirect(
            self,
            request: models.ModifyModuleIpDirectRequest,
            opts: Dict = None,
    ) -> models.ModifyModuleIpDirectResponse:
        """
        This API is used to modify the IP direct access of a module.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyModuleIpDirect"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyModuleIpDirectResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyModuleName(
            self,
            request: models.ModifyModuleNameRequest,
            opts: Dict = None,
    ) -> models.ModifyModuleNameResponse:
        """
        This API is used to rename a module.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyModuleName"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyModuleNameResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyModuleNetwork(
            self,
            request: models.ModifyModuleNetworkRequest,
            opts: Dict = None,
    ) -> models.ModifyModuleNetworkResponse:
        """
        This API is used to modify the default bandwidth cap of a module.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyModuleNetwork"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyModuleNetworkResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyModuleSecurityGroups(
            self,
            request: models.ModifyModuleSecurityGroupsRequest,
            opts: Dict = None,
    ) -> models.ModifyModuleSecurityGroupsResponse:
        """
        This API is used to modify the default security group of a module.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyModuleSecurityGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyModuleSecurityGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyPrivateIpAddressesAttribute(
            self,
            request: models.ModifyPrivateIpAddressesAttributeRequest,
            opts: Dict = None,
    ) -> models.ModifyPrivateIpAddressesAttributeResponse:
        """
        This API is used to modify the private IP attributes of an ENI.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyPrivateIpAddressesAttribute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyPrivateIpAddressesAttributeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyRouteTableAttribute(
            self,
            request: models.ModifyRouteTableAttributeRequest,
            opts: Dict = None,
    ) -> models.ModifyRouteTableAttributeResponse:
        """
        This API is used to modify the attributes of a route table.
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
        This API is used to modify the attributes of a security group.
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
        This API is used to modify the outbound and inbound rules of a security group.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifySecurityGroupPolicies"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifySecurityGroupPoliciesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifySubnetAttribute(
            self,
            request: models.ModifySubnetAttributeRequest,
            opts: Dict = None,
    ) -> models.ModifySubnetAttributeResponse:
        """
        This API is used to modify the attributes of a subnet.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifySubnetAttribute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifySubnetAttributeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyTargetPort(
            self,
            request: models.ModifyTargetPortRequest,
            opts: Dict = None,
    ) -> models.ModifyTargetPortResponse:
        """
        This API is used to modify the port of a real server bound to a listener.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyTargetPort"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyTargetPortResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyTargetWeight(
            self,
            request: models.ModifyTargetWeightRequest,
            opts: Dict = None,
    ) -> models.ModifyTargetWeightResponse:
        """
        This API is used to modify the forwarding weight of a real server bound to a listener.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyTargetWeight"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyTargetWeightResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyVpcAttribute(
            self,
            request: models.ModifyVpcAttributeRequest,
            opts: Dict = None,
    ) -> models.ModifyVpcAttributeResponse:
        """
        This API is used to modify the attributes of a VPC.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyVpcAttribute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyVpcAttributeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RebootInstances(
            self,
            request: models.RebootInstancesRequest,
            opts: Dict = None,
    ) -> models.RebootInstancesResponse:
        """
        This API is used to restart an instance. Only instances in `RUNNING` status can be restarted. The instance status will become `REBOOTING` when the API is called successfully and will become `RUNNING` when the instance is restarted successfully. Forced restart is supported. Just like powering off a physical PC and restarting it, a forced restart may cause data loss or file system corruption. Make sure that you use this API only when the server cannot be restarted normally.
        """
        
        kwargs = {}
        kwargs["action"] = "RebootInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RebootInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ReleaseAddresses(
            self,
            request: models.ReleaseAddressesRequest,
            opts: Dict = None,
    ) -> models.ReleaseAddressesResponse:
        """
        This API is used to release one or multiple EIPs.
        This operation is irreversible. Once you release an EIP, the IP address associated with it will no longer belong to you.
        Only EIPs in `UNBIND` status can be released.
        """
        
        kwargs = {}
        kwargs["action"] = "ReleaseAddresses"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ReleaseAddressesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ReleaseIpv6Addresses(
            self,
            request: models.ReleaseIpv6AddressesRequest,
            opts: Dict = None,
    ) -> models.ReleaseIpv6AddressesResponse:
        """
        This API is used to release the IPv6 addresses of an ENI.
        """
        
        kwargs = {}
        kwargs["action"] = "ReleaseIpv6Addresses"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ReleaseIpv6AddressesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RemovePrivateIpAddresses(
            self,
            request: models.RemovePrivateIpAddressesRequest,
            opts: Dict = None,
    ) -> models.RemovePrivateIpAddressesResponse:
        """
        This API is used to return the private IPs of an ENI.
        To return the secondary private IPs of an ENI, the API will automatically unbind them from the ENI. The primary private IP of the ENI cannot be returned.
        """
        
        kwargs = {}
        kwargs["action"] = "RemovePrivateIpAddresses"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RemovePrivateIpAddressesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ReplaceRouteTableAssociation(
            self,
            request: models.ReplaceRouteTableAssociationRequest,
            opts: Dict = None,
    ) -> models.ReplaceRouteTableAssociationResponse:
        """
        This API is used to modify the route table associated with a subnet. A subnet can be associated with only one route table.
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
        This API is used to replace a routing policy.
        """
        
        kwargs = {}
        kwargs["action"] = "ReplaceRoutes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ReplaceRoutesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ReplaceSecurityGroupPolicy(
            self,
            request: models.ReplaceSecurityGroupPolicyRequest,
            opts: Dict = None,
    ) -> models.ReplaceSecurityGroupPolicyResponse:
        """
        This API is used to replace a single routing rule of a security group. You can replace only one rule in a single direction in one request and must specify the index (PolicyIndex).
        """
        
        kwargs = {}
        kwargs["action"] = "ReplaceSecurityGroupPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ReplaceSecurityGroupPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ResetInstances(
            self,
            request: models.ResetInstancesRequest,
            opts: Dict = None,
    ) -> models.ResetInstancesResponse:
        """
        This API is used to reinstall an instance. If you specify the `ImageId` parameter, the specified image will be used; otherwise, the image used by the current instance will be used. If you don't specify the password, a password will be sent later in Message Center.
        """
        
        kwargs = {}
        kwargs["action"] = "ResetInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ResetInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ResetInstancesMaxBandwidth(
            self,
            request: models.ResetInstancesMaxBandwidthRequest,
            opts: Dict = None,
    ) -> models.ResetInstancesMaxBandwidthResponse:
        """
        This API is used to reset the bandwidth cap of an instance.
        """
        
        kwargs = {}
        kwargs["action"] = "ResetInstancesMaxBandwidth"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ResetInstancesMaxBandwidthResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ResetInstancesPassword(
            self,
            request: models.ResetInstancesPasswordRequest,
            opts: Dict = None,
    ) -> models.ResetInstancesPasswordResponse:
        """
        This API is used to reset the password for a running status. You need to explicitly specify the `ForceStop` parameter; otherwise, you can reset the password only for instances that have been shut down.
        """
        
        kwargs = {}
        kwargs["action"] = "ResetInstancesPassword"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ResetInstancesPasswordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ResetRoutes(
            self,
            request: models.ResetRoutesRequest,
            opts: Dict = None,
    ) -> models.ResetRoutesResponse:
        """
        This API is used to reset a route table name and all routing policies.
        """
        
        kwargs = {}
        kwargs["action"] = "ResetRoutes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ResetRoutesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RunInstances(
            self,
            request: models.RunInstancesRequest,
            opts: Dict = None,
    ) -> models.RunInstancesResponse:
        """
        This API is used to create an ECM instance.
        """
        
        kwargs = {}
        kwargs["action"] = "RunInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RunInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SetLoadBalancerSecurityGroups(
            self,
            request: models.SetLoadBalancerSecurityGroupsRequest,
            opts: Dict = None,
    ) -> models.SetLoadBalancerSecurityGroupsResponse:
        """
        This API is used to configure security groups for a CLB instance.
        """
        
        kwargs = {}
        kwargs["action"] = "SetLoadBalancerSecurityGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SetLoadBalancerSecurityGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SetSecurityGroupForLoadbalancers(
            self,
            request: models.SetSecurityGroupForLoadbalancersRequest,
            opts: Dict = None,
    ) -> models.SetSecurityGroupForLoadbalancersResponse:
        """
        This API is used to bind or unbind a security group to or from multiple CLB instances.
        """
        
        kwargs = {}
        kwargs["action"] = "SetSecurityGroupForLoadbalancers"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SetSecurityGroupForLoadbalancersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StartInstances(
            self,
            request: models.StartInstancesRequest,
            opts: Dict = None,
    ) -> models.StartInstancesResponse:
        """
        This API is used to start an instance. Only instances in `STOPPED` status can be started. The instance status will become `STARTING` when this API is called successfully and will become `RUNNING` when the instance is started successfully.
        """
        
        kwargs = {}
        kwargs["action"] = "StartInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StartInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StopInstances(
            self,
            request: models.StopInstancesRequest,
            opts: Dict = None,
    ) -> models.StopInstancesResponse:
        """
        Only instances in `RUNNING` status can be shut down.
        The instance status will become `STOPPING` when the API is called successfully and will become `STOPPED` when the instance is shut down successfully.
        Forced shutdown is supported. Just like powering off a physical PC, a forced shutdown may cause data loss or file system corruption. Make sure that you use this API only when the server cannot be shut down normally.
        """
        
        kwargs = {}
        kwargs["action"] = "StopInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StopInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def TerminateInstances(
            self,
            request: models.TerminateInstancesRequest,
            opts: Dict = None,
    ) -> models.TerminateInstancesResponse:
        """
        This API is used to terminate an instance.
        """
        
        kwargs = {}
        kwargs["action"] = "TerminateInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.TerminateInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)