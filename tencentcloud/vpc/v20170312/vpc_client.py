# -*- coding: utf8 -*-
# Copyright (c) 2017-2018 THL A29 Limited, a Tencent company. All Rights Reserved.
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
    _endpoint = 'vpc.tencentcloudapi.com'


    def AcceptAttachCcnInstances(self, request):
        """本接口（AcceptAttachCcnInstances）用于跨账号关联实例时，云联网所有者接受并同意关联操作。

        :param request: Request instance for AcceptAttachCcnInstances.
        :type request: :class:`tencentcloud.vpc.v20170312.models.AcceptAttachCcnInstancesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.AcceptAttachCcnInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AcceptAttachCcnInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AcceptAttachCcnInstancesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def AllocateAddresses(self, request):
        """This API is used to apply for one or more [Elastic IP Addresses](https://cloud.tencent.com/document/product/213/1941) (EIPs for short).
        * An EIP is a static IP address that is dedicated for dynamic cloud computing. You can quickly re-map an EIP to another instance under your account to protect against instance failures.
        * Your EIP is associated with your Tencent Cloud account rather than an instance. It remains associated with your Tencent Cloud account until you choose to explicitly release it or your account is in arrears for more than 24 hours.
        * The maximum number of EIPs that can be applied for a Tencent Cloud account in each region is restricted. For more information, see [EIP Product Introduction](https://cloud.tencent.com/document/product/213/5733). You can get the quota information through the DescribeAddressQuota API.

        :param request: Request instance for AllocateAddresses.
        :type request: :class:`tencentcloud.vpc.v20170312.models.AllocateAddressesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.AllocateAddressesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AllocateAddresses", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AllocateAddressesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def AssignIpv6Addresses(self, request):
        """本接口（AssignIpv6Addresses）用于弹性网卡申请`IPv6`地址。<br />
        本接口是异步完成，如需查询异步任务执行结果，请使用本接口返回的`RequestId`轮询`QueryTask`接口。
        * 一个弹性网卡支持绑定的IP地址是有限制的，更多资源限制信息详见<a href="/document/product/576/18527">弹性网卡使用限制</a>。
        * 可以指定`IPv6`地址申请，地址类型不能为主`IP`，`IPv6`地址暂时只支持作为辅助`IP`。
        * 地址必须要在弹性网卡所在子网内，而且不能被占用。
        * 在弹性网卡上申请一个到多个辅助`IPv6`地址，接口会在弹性网卡所在子网段内返回指定数量的辅助`IPv6`地址。

        :param request: Request instance for AssignIpv6Addresses.
        :type request: :class:`tencentcloud.vpc.v20170312.models.AssignIpv6AddressesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.AssignIpv6AddressesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AssignIpv6Addresses", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AssignIpv6AddressesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def AssignIpv6CidrBlock(self, request):
        """This API is used to assign IPv6 ranges.
        * To use this API, you must already have a VPC instance. If you do not have a VPC instance yet, use the <a href="https://cloud.tencent.com/document/api/215/15774" title="CreateVpc" target="_blank">CreateVpc</a> API to create one.
        * Each VPC can apply for only one IPv6 range.

        :param request: Request instance for AssignIpv6CidrBlock.
        :type request: :class:`tencentcloud.vpc.v20170312.models.AssignIpv6CidrBlockRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.AssignIpv6CidrBlockResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AssignIpv6CidrBlock", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AssignIpv6CidrBlockResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def AssignIpv6SubnetCidrBlock(self, request):
        """本接口（AssignIpv6SubnetCidrBlock）用于分配IPv6子网段。
        * 给子网分配 `IPv6` 网段，要求子网所属 `VPC` 已获得 `IPv6` 网段。如果尚未分配，请先通过接口 `AssignIpv6CidrBlock` 给子网所属 `VPC` 分配一个 `IPv6` 网段。否则无法分配 `IPv6` 子网段。
        * 每个子网只能分配一个IPv6网段。

        :param request: Request instance for AssignIpv6SubnetCidrBlock.
        :type request: :class:`tencentcloud.vpc.v20170312.models.AssignIpv6SubnetCidrBlockRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.AssignIpv6SubnetCidrBlockResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AssignIpv6SubnetCidrBlock", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AssignIpv6SubnetCidrBlockResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def AssociateAddress(self, request):
        """本接口 (AssociateAddress) 用于将[弹性公网IP](https://cloud.tencent.com/document/product/213/1941)（简称 EIP）绑定到实例或弹性网卡的指定内网 IP 上。
        * 将 EIP 绑定到实例（CVM）上，其本质是将 EIP 绑定到实例上主网卡的主内网 IP 上。
        * 将 EIP 绑定到主网卡的主内网IP上，绑定过程会把其上绑定的普通公网 IP 自动解绑并释放。
        * 将 EIP 绑定到指定网卡的内网 IP上（非主网卡的主内网IP），则必须先解绑该 EIP，才能再绑定新的。
        * 将 EIP 绑定到NAT网关，请使用接口[EipBindNatGateway](https://cloud.tencent.com/document/product/215/4093)
        * EIP 如果欠费或被封堵，则不能被绑定。
        * 只有状态为 UNBIND 的 EIP 才能够被绑定。

        :param request: Request instance for AssociateAddress.
        :type request: :class:`tencentcloud.vpc.v20170312.models.AssociateAddressRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.AssociateAddressResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AssociateAddress", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AssociateAddressResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def AttachCcnInstances(self, request):
        """本接口（AttachCcnInstances）用于将网络实例加载到云联网实例中，网络实例包括VPC和专线网关。<br />
        每个云联网能够关联的网络实例个数是有限的，详请参考产品文档。如果需要扩充请联系在线客服。

        :param request: Request instance for AttachCcnInstances.
        :type request: :class:`tencentcloud.vpc.v20170312.models.AttachCcnInstancesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.AttachCcnInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AttachCcnInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AttachCcnInstancesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def AttachClassicLinkVpc(self, request):
        """本接口(AttachClassicLinkVpc)用于创建私有网络和基础网络设备互通。
        * 私有网络和基础网络设备必须在同一个地域。
        * 私有网络和基础网络的区别详见vpc产品文档-<a href="https://cloud.tencent.com/document/product/215/535#2.-.E7.A7.81.E6.9C.89.E7.BD.91.E7.BB.9C.E4.B8.8E.E5.9F.BA.E7.A1.80.E7.BD.91.E7.BB.9C">私有网络与基础网络</a>。

        :param request: Request instance for AttachClassicLinkVpc.
        :type request: :class:`tencentcloud.vpc.v20170312.models.AttachClassicLinkVpcRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.AttachClassicLinkVpcResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AttachClassicLinkVpc", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AttachClassicLinkVpcResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def AttachNetworkInterface(self, request):
        """本接口（AttachNetworkInterface）用于弹性网卡绑定云主机。
        * 一个云主机可以绑定多个弹性网卡，但只能绑定一个主网卡。更多限制信息详见<a href="https://cloud.tencent.com/document/product/215/6513">弹性网卡使用限制</a>。
        * 一个弹性网卡只能同时绑定一个云主机。
        * 只有运行中或者已关机状态的云主机才能绑定弹性网卡，查看云主机状态详见<a href="https://cloud.tencent.com/document/api/213/9452#instance_state">腾讯云主机信息</a>。
        * 弹性网卡绑定的云主机必须是私有网络的，而且云主机所在可用区必须和弹性网卡子网的可用区相同。

        :param request: Request instance for AttachNetworkInterface.
        :type request: :class:`tencentcloud.vpc.v20170312.models.AttachNetworkInterfaceRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.AttachNetworkInterfaceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AttachNetworkInterface", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AttachNetworkInterfaceResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CheckNetDetectState(self, request):
        """This API is used to verify the network detection status.

        :param request: Request instance for CheckNetDetectState.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CheckNetDetectStateRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CheckNetDetectStateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CheckNetDetectState", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CheckNetDetectStateResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateAddressTemplate(self, request):
        """本接口（CreateAddressTemplate）用于创建IP地址模版

        :param request: Request instance for CreateAddressTemplate.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CreateAddressTemplateRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CreateAddressTemplateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateAddressTemplate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateAddressTemplateResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateAddressTemplateGroup(self, request):
        """本接口（CreateAddressTemplateGroup）用于创建IP地址模版集合

        :param request: Request instance for CreateAddressTemplateGroup.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CreateAddressTemplateGroupRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CreateAddressTemplateGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateAddressTemplateGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateAddressTemplateGroupResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateCcn(self, request):
        """本接口（CreateCcn）用于创建云联网（CCN）。<br />
        每个账号能创建的云联网实例个数是有限的，详请参考产品文档。如果需要扩充请联系在线客服。

        :param request: Request instance for CreateCcn.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CreateCcnRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CreateCcnResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateCcn", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateCcnResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateDefaultVpc(self, request):
        """This API is used to create a default VPC.

        The default VPC is suitable for getting started with and launching public instances, and it can be used like any other VPCs. To create a standard VPC, for which you need to specify a VPC name, VPC IP range, subnet IP range, and subnet availability zone, use the regular CreateVpc API.

        Under normal circumstances, this API may not create a default VPC. It depends on the network attributes (DescribeAccountAttributes) of your account.
        * If both basic network and VPC are supported, the returned VpcId is 0.
        * If only VPC is supported, the default VPC information is returned.

        You can also use the Force parameter to forcibly return a default VPC.

        :param request: Request instance for CreateDefaultVpc.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CreateDefaultVpcRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CreateDefaultVpcResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateDefaultVpc", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateDefaultVpcResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateDirectConnectGatewayCcnRoutes(self, request):
        """本接口（CreateDirectConnectGatewayCcnRoutes）用于创建专线网关的云联网路由（IDC网段）

        :param request: Request instance for CreateDirectConnectGatewayCcnRoutes.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CreateDirectConnectGatewayCcnRoutesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CreateDirectConnectGatewayCcnRoutesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateDirectConnectGatewayCcnRoutes", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateDirectConnectGatewayCcnRoutesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateHaVip(self, request):
        """本接口（CreateHaVip）用于创建高可用虚拟IP（HAVIP）

        :param request: Request instance for CreateHaVip.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CreateHaVipRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CreateHaVipResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateHaVip", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateHaVipResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateNatGateway(self, request):
        """本接口(CreateNatGateway)用于创建NAT网关。

        :param request: Request instance for CreateNatGateway.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CreateNatGatewayRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CreateNatGatewayResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateNatGateway", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateNatGatewayResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateNatGatewayDestinationIpPortTranslationNatRule(self, request):
        """本接口(CreateNatGatewayDestinationIpPortTranslationNatRule)用于创建NAT网关端口转发规则。

        :param request: Request instance for CreateNatGatewayDestinationIpPortTranslationNatRule.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CreateNatGatewayDestinationIpPortTranslationNatRuleRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CreateNatGatewayDestinationIpPortTranslationNatRuleResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateNatGatewayDestinationIpPortTranslationNatRule", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateNatGatewayDestinationIpPortTranslationNatRuleResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateNetDetect(self, request):
        """This API is used to create a network detection instance.

        :param request: Request instance for CreateNetDetect.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CreateNetDetectRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CreateNetDetectResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateNetDetect", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateNetDetectResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateNetworkInterface(self, request):
        """This API is used to create one or more ENIs.
        * You can specify private IP addresses and a primary IP when creating an ENI. The specified private IP must be in the same subnet as the ENI and is not occupied.
        * When creating an ENI, you can specify the number of private IP addresses that you want to apply for. The system will randomly generate private IP addresses.
        * An ENI can only be bound with a limited number of IP addresses. For more information about resource limits, see <a href="/document/product/576/18527">ENI Use Limits</a>.
        * You can bind an existing security group when creating an ENI.
        * You can bind a tag when creating an ENI. The tag list in the response indicates the tags that have been successfully added.

        :param request: Request instance for CreateNetworkInterface.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CreateNetworkInterfaceRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CreateNetworkInterfaceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateNetworkInterface", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateNetworkInterfaceResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateRouteTable(self, request):
        """本接口(CreateRouteTable)用于创建路由表。
        * 创建了VPC后，系统会创建一个默认路由表，所有新建的子网都会关联到默认路由表。默认情况下您可以直接使用默认路由表来管理您的路由策略。当您的路由策略较多时，您可以调用创建路由表接口创建更多路由表管理您的路由策略。

        :param request: Request instance for CreateRouteTable.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CreateRouteTableRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CreateRouteTableResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateRouteTable", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateRouteTableResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateRoutes(self, request):
        """本接口(CreateRoutes)用于创建路由策略。
        * 向指定路由表批量新增路由策略。

        :param request: Request instance for CreateRoutes.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CreateRoutesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CreateRoutesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateRoutes", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateRoutesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateSecurityGroup(self, request):
        """本接口（CreateSecurityGroup）用于创建新的安全组（SecurityGroup）。
        * 每个账户下每个地域的每个项目的<a href="https://cloud.tencent.com/document/product/213/500#2.-.E5.AE.89.E5.85.A8.E7.BB.84.E7.9A.84.E9.99.90.E5.88.B6">安全组数量限制</a>。
        * 新建的安全组的入站和出站规则默认都是全部拒绝，在创建后通常您需要再调用CreateSecurityGroupPolicies将安全组的规则设置为需要的规则。

        :param request: Request instance for CreateSecurityGroup.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CreateSecurityGroupRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CreateSecurityGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateSecurityGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateSecurityGroupResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateSecurityGroupPolicies(self, request):
        """This API is used to create security group policies (SecurityGroupPolicy).

        * The `Version` field indicates the version number of a security group policy, which will automatically increment by 1 every time you update the security policy, to prevent the expiration of the updated routing policies. If this field is left empty, any conflicts will be ignored.
        * The value of the `Protocol` field can be TCP, UDP, ICMP, ICMPV6, GRE, or ALL.
        * The `CidrBlock` field allows you to enter any string that conforms to the CIDR format. (More details) In a basic network, if a CidrBlock contains private IP addresses on Tencent Cloud for devices under your account other than CVMs, it does not mean this policy allows you to access these devices. The network isolation policies between tenants take priority over the private network policies in security groups.
        * The `Ipv6CidrBlock` field allows you to enter any string that conforms to the IPv6 CIDR format. (More details) In a basic network, if an Ipv6CidrBlock contains private IPv6 addresses on Tencent Cloud for devices under your account other than CVMs, it does not mean this policy allows you to access these devices. The network isolation policies between tenants take priority over the private network policies in security groups.
        * The SecurityGroupId field allows you to enter the IDs of security groups that are in the same project as the security group to be modified, including the ID of the security group itself, to represent private IP addresses of all CVMs under the security group. If this field is used, the policy will change without manual modification according to the CVM associated with the policy ID while being used to match network messages.
        * The Port field allows you to enter a single port number, or two port numbers separated by a minus sign to represent a port range, such as 80 or 8000-8010. The Port field is accepted only if the value of the Protocol field is TCP or UDP. In other words, if the value of the Protocol field is not TCP or UDP, Protocol and Port are exclusive and cannot be entered at the same time, otherwise an error will occur with the API.
        * The Action field only allows you to enter ACCEPT or DROP.
        * CidrBlock, Ipv6CidrBlock, SecurityGroupId, and AddressTemplate are exclusive and cannot be entered at the same time. Protocol + Port and ServiceTemplate are mutually exclusive and cannot be entered at the same time.
        * Only policies in one direction can be created in each request. If you need to specify the PolicyIndex parameter, the indexes of policies must be consistent.

        :param request: Request instance for CreateSecurityGroupPolicies.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CreateSecurityGroupPoliciesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CreateSecurityGroupPoliciesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateSecurityGroupPolicies", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateSecurityGroupPoliciesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateServiceTemplate(self, request):
        """本接口（CreateServiceTemplate）用于创建协议端口模板

        :param request: Request instance for CreateServiceTemplate.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CreateServiceTemplateRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CreateServiceTemplateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateServiceTemplate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateServiceTemplateResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateServiceTemplateGroup(self, request):
        """本接口（CreateServiceTemplateGroup）用于创建协议端口模板集合

        :param request: Request instance for CreateServiceTemplateGroup.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CreateServiceTemplateGroupRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CreateServiceTemplateGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateServiceTemplateGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateServiceTemplateGroupResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateSubnet(self, request):
        """This API (CreateSubnet) is used to create subnets.
        * You must create a VPC before creating a subnet.
        * After the subnet is successfully created, its IP address range cannot be modified. The subnet IP address range must fall within the VPC IP address range. They can be the same if the VPC has only one subnet. We recommend that you keep the subnet IP address range within the VPC IP address range to reserve IP address ranges for other subnets.
        * The subnet mask of the smallest IP address range that can be created is 28 (16 IP addresses), and that of the largest IP address range is 16 (65,536 IP addresses).
        * IP address ranges of different subnets cannot overlap with each other within the same VPC.
        * A subnet is automatically associated with the default route table once created.

        :param request: Request instance for CreateSubnet.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CreateSubnetRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CreateSubnetResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateSubnet", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateSubnetResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateSubnets(self, request):
        """This API (CreateSubnets) is used to create subnets in batches.
        * You must create a VPC before creating a subnet.
        * After the subnet is successfully created, its IP address range cannot be modified. The subnet IP address range must fall within the VPC IP address range. They can be the same if the VPC has only one subnet. We recommend that you keep the subnet IP address range within the VPC IP address range to reserve IP address ranges for other subnets.
        * The subnet mask of the smallest IP address range that can be created is 28 (16 IP addresses), and that of the largest IP address range is 16 (65,536 IP addresses).
        * IP address ranges of different subnets cannot overlap with each other within the same VPC.
        * A subnet is automatically associated with the default route table once created.

        :param request: Request instance for CreateSubnets.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CreateSubnetsRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CreateSubnetsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateSubnets", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateSubnetsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateVpc(self, request):
        """本接口(CreateVpc)用于创建私有网络(VPC)。
        * 用户可以创建的最小网段子网掩码为28（有16个IP地址），最大网段子网掩码为16（65,536个IP地址）,如果规划VPC网段请参见VPC网段规划说明。
        * 同一个地域能创建的VPC资源个数也是有限制的，详见 <a href="https://cloud.tencent.com/doc/product/215/537" title="VPC使用限制">VPC使用限制</a>,如果需要扩充请联系在线客服。

        :param request: Request instance for CreateVpc.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CreateVpcRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CreateVpcResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateVpc", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateVpcResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateVpnConnection(self, request):
        """本接口（CreateVpnConnection）用于创建VPN通道。

        :param request: Request instance for CreateVpnConnection.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CreateVpnConnectionRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CreateVpnConnectionResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateVpnConnection", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateVpnConnectionResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateVpnGateway(self, request):
        """本接口（CreateVpnGateway）用于创建VPN网关。

        :param request: Request instance for CreateVpnGateway.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CreateVpnGatewayRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CreateVpnGatewayResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateVpnGateway", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateVpnGatewayResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteAddressTemplate(self, request):
        """本接口（DeleteAddressTemplate）用于删除IP地址模板

        :param request: Request instance for DeleteAddressTemplate.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DeleteAddressTemplateRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DeleteAddressTemplateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteAddressTemplate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteAddressTemplateResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteAddressTemplateGroup(self, request):
        """本接口（DeleteAddressTemplateGroup）用于删除IP地址模板集合

        :param request: Request instance for DeleteAddressTemplateGroup.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DeleteAddressTemplateGroupRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DeleteAddressTemplateGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteAddressTemplateGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteAddressTemplateGroupResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteCcn(self, request):
        """本接口（DeleteCcn）用于删除云联网。
        * 删除后，云联网关联的所有实例间路由将被删除，网络将会中断，请务必确认
        * 删除云联网是不可逆的操作，请谨慎处理。

        :param request: Request instance for DeleteCcn.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DeleteCcnRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DeleteCcnResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteCcn", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteCcnResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteDirectConnectGatewayCcnRoutes(self, request):
        """本接口（DeleteDirectConnectGatewayCcnRoutes）用于删除专线网关的云联网路由（IDC网段）

        :param request: Request instance for DeleteDirectConnectGatewayCcnRoutes.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DeleteDirectConnectGatewayCcnRoutesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DeleteDirectConnectGatewayCcnRoutesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteDirectConnectGatewayCcnRoutes", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteDirectConnectGatewayCcnRoutesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteHaVip(self, request):
        """本接口（DeleteHaVip）用于删除高可用虚拟IP（HAVIP）<br />
        本接口是异步完成，如需查询异步任务执行结果，请使用本接口返回的`RequestId`轮询`QueryTask`接口

        :param request: Request instance for DeleteHaVip.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DeleteHaVipRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DeleteHaVipResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteHaVip", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteHaVipResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteNatGateway(self, request):
        """本接口（DeleteNatGateway）用于删除NAT网关。
        删除 NAT 网关后，系统会自动删除路由表中包含此 NAT 网关的路由项，同时也会解绑弹性公网IP（EIP）。

        :param request: Request instance for DeleteNatGateway.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DeleteNatGatewayRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DeleteNatGatewayResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteNatGateway", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteNatGatewayResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteNatGatewayDestinationIpPortTranslationNatRule(self, request):
        """本接口（DeleteNatGatewayDestinationIpPortTranslationNatRule）用于删除NAT网关端口转发规则。

        :param request: Request instance for DeleteNatGatewayDestinationIpPortTranslationNatRule.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DeleteNatGatewayDestinationIpPortTranslationNatRuleRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DeleteNatGatewayDestinationIpPortTranslationNatRuleResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteNatGatewayDestinationIpPortTranslationNatRule", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteNatGatewayDestinationIpPortTranslationNatRuleResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteNetDetect(self, request):
        """This API (DeleteNetDetect) is used to delete a network detection instance.

        :param request: Request instance for DeleteNetDetect.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DeleteNetDetectRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DeleteNetDetectResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteNetDetect", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteNetDetectResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteNetworkInterface(self, request):
        """This API (DeleteNetworkInterface) is used to delete ENIs.
        * An ENI that has been bound to a CVM cannot be deleted.
        * An ENI can be deleted only after being unbound from the server. After the deletion, all private IP addresses associated with the ENI will be released.

        :param request: Request instance for DeleteNetworkInterface.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DeleteNetworkInterfaceRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DeleteNetworkInterfaceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteNetworkInterface", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteNetworkInterfaceResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteRouteTable(self, request):
        """删除路由表

        :param request: Request instance for DeleteRouteTable.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DeleteRouteTableRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DeleteRouteTableResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteRouteTable", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteRouteTableResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteRoutes(self, request):
        """本接口(DeleteRoutes)用于对某个路由表批量删除路由策略（Route）。

        :param request: Request instance for DeleteRoutes.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DeleteRoutesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DeleteRoutesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteRoutes", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteRoutesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteSecurityGroup(self, request):
        """本接口（DeleteSecurityGroup）用于删除安全组（SecurityGroup）。
        * 只有当前账号下的安全组允许被删除。
        * 安全组实例ID如果在其他安全组的规则中被引用，则无法直接删除。这种情况下，需要先进行规则修改，再删除安全组。
        * 删除的安全组无法再找回，请谨慎调用。

        :param request: Request instance for DeleteSecurityGroup.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DeleteSecurityGroupRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DeleteSecurityGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteSecurityGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteSecurityGroupResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteSecurityGroupPolicies(self, request):
        """本接口（DeleteSecurityGroupPolicies）用于用于删除安全组规则（SecurityGroupPolicy）。
        * SecurityGroupPolicySet.Version 用于指定要操作的安全组的版本。传入 Version 版本号若不等于当前安全组的最新版本，将返回失败；若不传 Version 则直接删除指定PolicyIndex的规则。

        :param request: Request instance for DeleteSecurityGroupPolicies.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DeleteSecurityGroupPoliciesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DeleteSecurityGroupPoliciesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteSecurityGroupPolicies", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteSecurityGroupPoliciesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteServiceTemplate(self, request):
        """本接口（DeleteServiceTemplate）用于删除协议端口模板

        :param request: Request instance for DeleteServiceTemplate.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DeleteServiceTemplateRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DeleteServiceTemplateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteServiceTemplate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteServiceTemplateResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteServiceTemplateGroup(self, request):
        """本接口（DeleteServiceTemplateGroup）用于删除协议端口模板集合

        :param request: Request instance for DeleteServiceTemplateGroup.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DeleteServiceTemplateGroupRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DeleteServiceTemplateGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteServiceTemplateGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteServiceTemplateGroupResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteSubnet(self, request):
        """This API (DeleteSubnet) is used to delete subnets.
        Before deleting a subnet, you need to remove all resources in the subnet, including CVMs, load balancers, cloud data, NoSQL databases, and ENIs.

        :param request: Request instance for DeleteSubnet.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DeleteSubnetRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DeleteSubnetResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteSubnet", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteSubnetResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


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
            body = self.call("DeleteVpc", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteVpcResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteVpnConnection(self, request):
        """本接口(DeleteVpnConnection)用于删除VPN通道。

        :param request: Request instance for DeleteVpnConnection.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DeleteVpnConnectionRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DeleteVpnConnectionResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteVpnConnection", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteVpnConnectionResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteVpnGateway(self, request):
        """本接口（DeleteVpnGateway）用于删除VPN网关。目前只支持删除运行中的按量计费的IPSEC网关实例。

        :param request: Request instance for DeleteVpnGateway.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DeleteVpnGatewayRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DeleteVpnGatewayResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteVpnGateway", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteVpnGatewayResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAccountAttributes(self, request):
        """本接口（DescribeAccountAttributes）用于查询用户账号私有属性。

        :param request: Request instance for DescribeAccountAttributes.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeAccountAttributesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeAccountAttributesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAccountAttributes", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAccountAttributesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAddressQuota(self, request):
        """本接口 (DescribeAddressQuota) 用于查询您账户的[弹性公网IP](https://cloud.tencent.com/document/product/213/1941)（简称 EIP）在当前地域的配额信息。配额详情可参见 [EIP 产品简介](https://cloud.tencent.com/document/product/213/5733)。

        :param request: Request instance for DescribeAddressQuota.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeAddressQuotaRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeAddressQuotaResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAddressQuota", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAddressQuotaResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAddressTemplateGroups(self, request):
        """本接口（DescribeAddressTemplateGroups）用于查询IP地址模板集合

        :param request: Request instance for DescribeAddressTemplateGroups.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeAddressTemplateGroupsRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeAddressTemplateGroupsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAddressTemplateGroups", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAddressTemplateGroupsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAddressTemplates(self, request):
        """本接口（DescribeAddressTemplates）用于查询IP地址模板

        :param request: Request instance for DescribeAddressTemplates.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeAddressTemplatesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeAddressTemplatesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAddressTemplates", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAddressTemplatesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAddresses(self, request):
        """本接口 (DescribeAddresses) 用于查询一个或多个[弹性公网IP](https://cloud.tencent.com/document/product/213/1941)（简称 EIP）的详细信息。
        * 如果参数为空，返回当前用户一定数量（Limit所指定的数量，默认为20）的 EIP。

        :param request: Request instance for DescribeAddresses.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeAddressesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeAddressesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAddresses", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAddressesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeCcnAttachedInstances(self, request):
        """本接口（DescribeCcnAttachedInstances）用于查询云联网实例下已关联的网络实例。

        :param request: Request instance for DescribeCcnAttachedInstances.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeCcnAttachedInstancesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeCcnAttachedInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeCcnAttachedInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeCcnAttachedInstancesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeCcnRoutes(self, request):
        """本接口（DescribeCcnRoutes）用于查询已加入云联网（CCN）的路由

        :param request: Request instance for DescribeCcnRoutes.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeCcnRoutesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeCcnRoutesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeCcnRoutes", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeCcnRoutesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeCcns(self, request):
        """本接口（DescribeCcns）用于查询云联网（CCN）列表。

        :param request: Request instance for DescribeCcns.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeCcnsRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeCcnsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeCcns", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeCcnsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeClassicLinkInstances(self, request):
        """本接口(DescribeClassicLinkInstances)用于查询私有网络和基础网络设备互通列表。

        :param request: Request instance for DescribeClassicLinkInstances.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeClassicLinkInstancesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeClassicLinkInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeClassicLinkInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeClassicLinkInstancesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeDirectConnectGatewayCcnRoutes(self, request):
        """本接口（DescribeDirectConnectGatewayCcnRoutes）用于查询专线网关的云联网路由（IDC网段）

        :param request: Request instance for DescribeDirectConnectGatewayCcnRoutes.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeDirectConnectGatewayCcnRoutesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeDirectConnectGatewayCcnRoutesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDirectConnectGatewayCcnRoutes", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDirectConnectGatewayCcnRoutesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeGatewayFlowMonitorDetail(self, request):
        """本接口（DescribeGatewayFlowMonitorDetail）用于查询网关流量监控明细。
        * 只支持单个网关实例查询。即入参 `VpnId` `DirectConnectGatewayId` `PeeringConnectionId` `NatId` 最多只支持传一个，且必须传一个。
        * 如果网关有流量，但调用本接口没有返回数据，请在控制台对应网关详情页确认是否开启网关流量监控。

        :param request: Request instance for DescribeGatewayFlowMonitorDetail.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeGatewayFlowMonitorDetailRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeGatewayFlowMonitorDetailResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeGatewayFlowMonitorDetail", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeGatewayFlowMonitorDetailResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeHaVips(self, request):
        """本接口（DescribeHaVips）用于查询高可用虚拟IP（HAVIP）列表。

        :param request: Request instance for DescribeHaVips.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeHaVipsRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeHaVipsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeHaVips", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeHaVipsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeNatGatewayDestinationIpPortTranslationNatRules(self, request):
        """本接口（DescribeNatGatewayDestinationIpPortTranslationNatRules）用于查询NAT网关端口转发规则对象数组。

        :param request: Request instance for DescribeNatGatewayDestinationIpPortTranslationNatRules.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeNatGatewayDestinationIpPortTranslationNatRulesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeNatGatewayDestinationIpPortTranslationNatRulesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeNatGatewayDestinationIpPortTranslationNatRules", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeNatGatewayDestinationIpPortTranslationNatRulesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeNatGateways(self, request):
        """本接口（DescribeNatGateways）用于查询 NAT 网关。

        :param request: Request instance for DescribeNatGateways.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeNatGatewaysRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeNatGatewaysResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeNatGateways", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeNatGatewaysResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeNetDetectStates(self, request):
        """This API (DescribeNetDetectStates) is used to query the list of network detection verification results.

        :param request: Request instance for DescribeNetDetectStates.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeNetDetectStatesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeNetDetectStatesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeNetDetectStates", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeNetDetectStatesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeNetDetects(self, request):
        """This API (DescribeNetDetects) is used to query the list of network detection instances.

        :param request: Request instance for DescribeNetDetects.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeNetDetectsRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeNetDetectsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeNetDetects", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeNetDetectsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeNetworkInterfaceLimit(self, request):
        """This API (DescribeNetworkInterfaceLimit) is used to query the ENI quota based on the CVM instance ID. It returns the ENI quota to which the CVM instance can be bound and the IP address quota that can be allocated to each ENI.

        :param request: Request instance for DescribeNetworkInterfaceLimit.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeNetworkInterfaceLimitRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeNetworkInterfaceLimitResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeNetworkInterfaceLimit", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeNetworkInterfaceLimitResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeSecurityGroupAssociationStatistics(self, request):
        """本接口（DescribeSecurityGroupAssociationStatistics）用于查询安全组关联的实例统计。

        :param request: Request instance for DescribeSecurityGroupAssociationStatistics.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeSecurityGroupAssociationStatisticsRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeSecurityGroupAssociationStatisticsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeSecurityGroupAssociationStatistics", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSecurityGroupAssociationStatisticsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeSecurityGroupPolicies(self, request):
        """本接口（DescribeSecurityGroupPolicies）用于查询安全组规则。

        :param request: Request instance for DescribeSecurityGroupPolicies.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeSecurityGroupPoliciesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeSecurityGroupPoliciesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeSecurityGroupPolicies", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSecurityGroupPoliciesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeSecurityGroups(self, request):
        """本接口（DescribeSecurityGroups）用于查询安全组。

        :param request: Request instance for DescribeSecurityGroups.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeSecurityGroupsRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeSecurityGroupsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeSecurityGroups", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSecurityGroupsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeServiceTemplateGroups(self, request):
        """本接口（DescribeServiceTemplateGroups）用于查询协议端口模板集合

        :param request: Request instance for DescribeServiceTemplateGroups.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeServiceTemplateGroupsRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeServiceTemplateGroupsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeServiceTemplateGroups", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeServiceTemplateGroupsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeServiceTemplates(self, request):
        """本接口（DescribeServiceTemplates）用于查询协议端口模板

        :param request: Request instance for DescribeServiceTemplates.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeServiceTemplatesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeServiceTemplatesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeServiceTemplates", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeServiceTemplatesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeSubnets(self, request):
        """本接口（DescribeSubnets）用于查询子网列表。

        :param request: Request instance for DescribeSubnets.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeSubnetsRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeSubnetsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeSubnets", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSubnetsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeTaskResult(self, request):
        """查询EIP异步任务执行结果

        :param request: Request instance for DescribeTaskResult.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeTaskResultRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeTaskResultResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeTaskResult", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTaskResultResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeVpcIpv6Addresses(self, request):
        """本接口（DescribeVpcIpv6Addresses）用于查询 `VPC` `IPv6` 信息。
        只能查询已使用的`IPv6`信息，当查询未使用的IP时，本接口不会报错，但不会出现在返回结果里。

        :param request: Request instance for DescribeVpcIpv6Addresses.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeVpcIpv6AddressesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeVpcIpv6AddressesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeVpcIpv6Addresses", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeVpcIpv6AddressesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeVpcPrivateIpAddresses(self, request):
        """本接口（DescribeVpcPrivateIpAddresses）用于查询VPC内网IP信息。<br />
        只能查询已使用的IP信息，当查询未使用的IP时，本接口不会报错，但不会出现在返回结果里。

        :param request: Request instance for DescribeVpcPrivateIpAddresses.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeVpcPrivateIpAddressesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeVpcPrivateIpAddressesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeVpcPrivateIpAddresses", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeVpcPrivateIpAddressesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeVpcs(self, request):
        """本接口（DescribeVpcs）用于查询私有网络列表。

        :param request: Request instance for DescribeVpcs.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeVpcsRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeVpcsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeVpcs", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeVpcsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeVpnConnections(self, request):
        """本接口（DescribeVpnConnections）查询VPN通道列表。

        :param request: Request instance for DescribeVpnConnections.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeVpnConnectionsRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeVpnConnectionsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeVpnConnections", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeVpnConnectionsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeVpnGateways(self, request):
        """本接口（DescribeVpnGateways）用于查询VPN网关列表。

        :param request: Request instance for DescribeVpnGateways.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeVpnGatewaysRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeVpnGatewaysResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeVpnGateways", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeVpnGatewaysResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DetachCcnInstances(self, request):
        """本接口（DetachCcnInstances）用于从云联网实例中解关联指定的网络实例。<br />
        解关联网络实例后，相应的路由策略会一并删除。

        :param request: Request instance for DetachCcnInstances.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DetachCcnInstancesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DetachCcnInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DetachCcnInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DetachCcnInstancesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DetachClassicLinkVpc(self, request):
        """本接口(DetachClassicLinkVpc)用于删除私有网络和基础网络设备互通。

        :param request: Request instance for DetachClassicLinkVpc.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DetachClassicLinkVpcRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DetachClassicLinkVpcResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DetachClassicLinkVpc", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DetachClassicLinkVpcResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DetachNetworkInterface(self, request):
        """本接口（DetachNetworkInterface）用于弹性网卡解绑云主机。

        :param request: Request instance for DetachNetworkInterface.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DetachNetworkInterfaceRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DetachNetworkInterfaceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DetachNetworkInterface", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DetachNetworkInterfaceResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DisableCcnRoutes(self, request):
        """本接口（DisableCcnRoutes）用于禁用已经启用的云联网（CCN）路由

        :param request: Request instance for DisableCcnRoutes.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DisableCcnRoutesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DisableCcnRoutesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DisableCcnRoutes", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DisableCcnRoutesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DisassociateAddress(self, request):
        """本接口 (DisassociateAddress) 用于解绑[弹性公网IP](https://cloud.tencent.com/document/product/213/1941)（简称 EIP）。
        * 支持CVM实例，弹性网卡上的EIP解绑
        * 不支持NAT上的EIP解绑。NAT上的EIP解绑请参考[EipUnBindNatGateway](https://cloud.tencent.com/document/product/215/4092)
        * 只有状态为 BIND 和 BIND_ENI 的 EIP 才能进行解绑定操作。
        * EIP 如果被封堵，则不能进行解绑定操作。

        :param request: Request instance for DisassociateAddress.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DisassociateAddressRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DisassociateAddressResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DisassociateAddress", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DisassociateAddressResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DisassociateNatGatewayAddress(self, request):
        """本接口（DisassociateNatGatewayAddress）用于NAT网关解绑弹性IP。

        :param request: Request instance for DisassociateNatGatewayAddress.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DisassociateNatGatewayAddressRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DisassociateNatGatewayAddressResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DisassociateNatGatewayAddress", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DisassociateNatGatewayAddressResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DownloadCustomerGatewayConfiguration(self, request):
        """本接口(DownloadCustomerGatewayConfiguration)用于下载VPN通道配置。

        :param request: Request instance for DownloadCustomerGatewayConfiguration.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DownloadCustomerGatewayConfigurationRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DownloadCustomerGatewayConfigurationResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DownloadCustomerGatewayConfiguration", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DownloadCustomerGatewayConfigurationResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def EnableCcnRoutes(self, request):
        """本接口（EnableCcnRoutes）用于启用已经加入云联网（CCN）的路由。<br />
        本接口会校验启用后，是否与已有路由冲突，如果冲突，则无法启用，失败处理。路由冲突时，需要先禁用与之冲突的路由，才能启用该路由。

        :param request: Request instance for EnableCcnRoutes.
        :type request: :class:`tencentcloud.vpc.v20170312.models.EnableCcnRoutesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.EnableCcnRoutesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("EnableCcnRoutes", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.EnableCcnRoutesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def HaVipAssociateAddressIp(self, request):
        """本接口（HaVipAssociateAddressIp）用于高可用虚拟IP（HAVIP）绑定弹性公网IP（EIP）<br />
        本接口是异步完成，如需查询异步任务执行结果，请使用本接口返回的`RequestId`轮询`QueryTask`接口

        :param request: Request instance for HaVipAssociateAddressIp.
        :type request: :class:`tencentcloud.vpc.v20170312.models.HaVipAssociateAddressIpRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.HaVipAssociateAddressIpResponse`

        """
        try:
            params = request._serialize()
            body = self.call("HaVipAssociateAddressIp", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.HaVipAssociateAddressIpResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def HaVipDisassociateAddressIp(self, request):
        """本接口（HaVipDisassociateAddressIp）用于将高可用虚拟IP（HAVIP）已绑定的弹性公网IP（EIP）解除绑定<br />
        本接口是异步完成，如需查询异步任务执行结果，请使用本接口返回的`RequestId`轮询`QueryTask`接口

        :param request: Request instance for HaVipDisassociateAddressIp.
        :type request: :class:`tencentcloud.vpc.v20170312.models.HaVipDisassociateAddressIpRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.HaVipDisassociateAddressIpResponse`

        """
        try:
            params = request._serialize()
            body = self.call("HaVipDisassociateAddressIp", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.HaVipDisassociateAddressIpResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def InquiryPriceCreateVpnGateway(self, request):
        """本接口（InquiryPriceCreateVpnGateway）用于创建VPN网关询价。

        :param request: Request instance for InquiryPriceCreateVpnGateway.
        :type request: :class:`tencentcloud.vpc.v20170312.models.InquiryPriceCreateVpnGatewayRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.InquiryPriceCreateVpnGatewayResponse`

        """
        try:
            params = request._serialize()
            body = self.call("InquiryPriceCreateVpnGateway", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.InquiryPriceCreateVpnGatewayResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def MigrateNetworkInterface(self, request):
        """本接口（MigrateNetworkInterface）用于弹性网卡迁移。

        :param request: Request instance for MigrateNetworkInterface.
        :type request: :class:`tencentcloud.vpc.v20170312.models.MigrateNetworkInterfaceRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.MigrateNetworkInterfaceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("MigrateNetworkInterface", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.MigrateNetworkInterfaceResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def MigratePrivateIpAddress(self, request):
        """本接口（MigratePrivateIpAddress）用于弹性网卡内网IP迁移。

        * 该接口用于将一个内网IP从一个弹性网卡上迁移到另外一个弹性网卡，主IP地址不支持迁移。
        * 迁移前后的弹性网卡必须在同一个子网内。

        :param request: Request instance for MigratePrivateIpAddress.
        :type request: :class:`tencentcloud.vpc.v20170312.models.MigratePrivateIpAddressRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.MigratePrivateIpAddressResponse`

        """
        try:
            params = request._serialize()
            body = self.call("MigratePrivateIpAddress", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.MigratePrivateIpAddressResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyAddressAttribute(self, request):
        """本接口 (ModifyAddressAttribute) 用于修改[弹性公网IP](https://cloud.tencent.com/document/product/213/1941)（简称 EIP）的名称。

        :param request: Request instance for ModifyAddressAttribute.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyAddressAttributeRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyAddressAttributeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyAddressAttribute", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyAddressAttributeResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyAddressTemplateAttribute(self, request):
        """本接口（ModifyAddressTemplateAttribute）用于修改IP地址模板

        :param request: Request instance for ModifyAddressTemplateAttribute.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyAddressTemplateAttributeRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyAddressTemplateAttributeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyAddressTemplateAttribute", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyAddressTemplateAttributeResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyAddressTemplateGroupAttribute(self, request):
        """本接口（ModifyAddressTemplateGroupAttribute）用于修改IP地址模板集合

        :param request: Request instance for ModifyAddressTemplateGroupAttribute.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyAddressTemplateGroupAttributeRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyAddressTemplateGroupAttributeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyAddressTemplateGroupAttribute", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyAddressTemplateGroupAttributeResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyAddressesBandwidth(self, request):
        """本接口（ModifyAddressesBandwidth）用于调整[弹性公网IP](https://cloud.tencent.com/document/product/213/1941)(简称EIP)带宽，包括后付费EIP, 预付费EIP和带宽包EIP

        :param request: Request instance for ModifyAddressesBandwidth.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyAddressesBandwidthRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyAddressesBandwidthResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyAddressesBandwidth", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyAddressesBandwidthResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyCcnAttribute(self, request):
        """本接口（ModifyCcnAttribute）用于修改云联网（CCN）的相关属性。

        :param request: Request instance for ModifyCcnAttribute.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyCcnAttributeRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyCcnAttributeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyCcnAttribute", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyCcnAttributeResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyHaVipAttribute(self, request):
        """本接口（ModifyHaVipAttribute）用于修改高可用虚拟IP（HAVIP）属性

        :param request: Request instance for ModifyHaVipAttribute.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyHaVipAttributeRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyHaVipAttributeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyHaVipAttribute", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyHaVipAttributeResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyIpv6AddressesAttribute(self, request):
        """本接口（ModifyIpv6AddressesAttribute）用于修改弹性网卡内网IPv6地址属性。

        :param request: Request instance for ModifyIpv6AddressesAttribute.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyIpv6AddressesAttributeRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyIpv6AddressesAttributeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyIpv6AddressesAttribute", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyIpv6AddressesAttributeResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyNatGatewayAttribute(self, request):
        """本接口（ModifyNatGatewayAttribute）用于修改NAT网关的属性。

        :param request: Request instance for ModifyNatGatewayAttribute.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyNatGatewayAttributeRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyNatGatewayAttributeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyNatGatewayAttribute", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyNatGatewayAttributeResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyNatGatewayDestinationIpPortTranslationNatRule(self, request):
        """本接口（ModifyNatGatewayDestinationIpPortTranslationNatRule）用于修改NAT网关端口转发规则。

        :param request: Request instance for ModifyNatGatewayDestinationIpPortTranslationNatRule.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyNatGatewayDestinationIpPortTranslationNatRuleRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyNatGatewayDestinationIpPortTranslationNatRuleResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyNatGatewayDestinationIpPortTranslationNatRule", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyNatGatewayDestinationIpPortTranslationNatRuleResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyNetDetect(self, request):
        """This API (ModifyNetDetect) is used to modify network detection parameters.

        :param request: Request instance for ModifyNetDetect.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyNetDetectRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyNetDetectResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyNetDetect", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyNetDetectResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyNetworkInterfaceAttribute(self, request):
        """本接口（ModifyNetworkInterfaceAttribute）用于修改弹性网卡属性。

        :param request: Request instance for ModifyNetworkInterfaceAttribute.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyNetworkInterfaceAttributeRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyNetworkInterfaceAttributeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyNetworkInterfaceAttribute", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyNetworkInterfaceAttributeResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyPrivateIpAddressesAttribute(self, request):
        """本接口（ModifyPrivateIpAddressesAttribute）用于修改弹性网卡内网IP属性。

        :param request: Request instance for ModifyPrivateIpAddressesAttribute.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyPrivateIpAddressesAttributeRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyPrivateIpAddressesAttributeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyPrivateIpAddressesAttribute", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyPrivateIpAddressesAttributeResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyRouteTableAttribute(self, request):
        """本接口（ModifyRouteTableAttribute）用于修改路由表（RouteTable）属性。

        :param request: Request instance for ModifyRouteTableAttribute.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyRouteTableAttributeRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyRouteTableAttributeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyRouteTableAttribute", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyRouteTableAttributeResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifySecurityGroupAttribute(self, request):
        """本接口（ModifySecurityGroupAttribute）用于修改安全组（SecurityGroupPolicy）属性。

        :param request: Request instance for ModifySecurityGroupAttribute.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifySecurityGroupAttributeRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifySecurityGroupAttributeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifySecurityGroupAttribute", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifySecurityGroupAttributeResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifySecurityGroupPolicies(self, request):
        """This API (ModifySecurityGroupPolicies) is used to reset the egress and ingress policies (SecurityGroupPolicy) of a security group.

        * This API deletes all the current egress and ingress policies, and then adds new Egress and Ingress policies. It does not support custom PolicyIndex indexes.
        * If SecurityGroupPolicySet.Version is set to 0, all policies will be cleared, and Egress and Ingress will be ignored.
        * The value of the Protocol field can be TCP, UDP, ICMP, ICMPV6, GRE, or ALL.
        * The CidrBlock field allows you to enter any string that conforms to the CIDR format. (More details) In a basic network, if a CidrBlock contains private IP addresses on Tencent Cloud for devices under your account other than CVMs, it does not mean this policy allows you to access these devices. The network isolation policies between tenants take priority over the private network policies in security groups.
        * The Ipv6CidrBlock field allows you to enter any string that conforms to the IPv6 CIDR format. (More details) In a basic network, if an Ipv6CidrBlock contains private IPv6 addresses on Tencent Cloud for devices under your account other than CVMs, it does not mean this policy allows you to access these devices. The network isolation policies between tenants take priority over the private network policies in security groups.
        * The SecurityGroupId field allows you to enter the IDs of security groups that are in the same project as the security group to be modified, including the ID of the security group itself, to represent private IP addresses of all CVMs under the security group. If this field is used, this policy will change without manual modification according to the CVM associated with the policy ID while being used to match network messages.
        * The Port field allows you to enter a single port number, or two port numbers separated by a minus sign to represent a port range, such as 80 or 8000-8010. The Port field can be used only when the value of the Protocol field is TCP or UDP.
        * The Action field only allows you to enter ACCEPT or DROP.
        * CidrBlock, Ipv6CidrBlock, SecurityGroupId, and AddressTemplate are exclusive and cannot be entered at the same time. Protocol + Port and ServiceTemplate are mutually exclusive and cannot be entered at the same time.

        :param request: Request instance for ModifySecurityGroupPolicies.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifySecurityGroupPoliciesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifySecurityGroupPoliciesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifySecurityGroupPolicies", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifySecurityGroupPoliciesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyServiceTemplateAttribute(self, request):
        """本接口（ModifyServiceTemplateAttribute）用于修改协议端口模板

        :param request: Request instance for ModifyServiceTemplateAttribute.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyServiceTemplateAttributeRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyServiceTemplateAttributeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyServiceTemplateAttribute", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyServiceTemplateAttributeResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyServiceTemplateGroupAttribute(self, request):
        """本接口（ModifyServiceTemplateGroupAttribute）用于修改协议端口模板集合。

        :param request: Request instance for ModifyServiceTemplateGroupAttribute.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyServiceTemplateGroupAttributeRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyServiceTemplateGroupAttributeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyServiceTemplateGroupAttribute", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyServiceTemplateGroupAttributeResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifySubnetAttribute(self, request):
        """本接口（ModifySubnetAttribute）用于修改子网属性。

        :param request: Request instance for ModifySubnetAttribute.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifySubnetAttributeRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifySubnetAttributeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifySubnetAttribute", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifySubnetAttributeResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyVpcAttribute(self, request):
        """本接口（ModifyVpcAttribute）用于修改私有网络（VPC）的相关属性。

        :param request: Request instance for ModifyVpcAttribute.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyVpcAttributeRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyVpcAttributeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyVpcAttribute", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyVpcAttributeResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyVpnConnectionAttribute(self, request):
        """本接口（ModifyVpnConnectionAttribute）用于修改VPN通道。

        :param request: Request instance for ModifyVpnConnectionAttribute.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyVpnConnectionAttributeRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyVpnConnectionAttributeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyVpnConnectionAttribute", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyVpnConnectionAttributeResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyVpnGatewayAttribute(self, request):
        """本接口（ModifyVpnGatewayAttribute）用于修改VPN网关属性。

        :param request: Request instance for ModifyVpnGatewayAttribute.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyVpnGatewayAttributeRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyVpnGatewayAttributeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyVpnGatewayAttribute", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyVpnGatewayAttributeResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def RejectAttachCcnInstances(self, request):
        """本接口（RejectAttachCcnInstances）用于跨账号关联实例时，云联网所有者拒绝关联操作。

        :param request: Request instance for RejectAttachCcnInstances.
        :type request: :class:`tencentcloud.vpc.v20170312.models.RejectAttachCcnInstancesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.RejectAttachCcnInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("RejectAttachCcnInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RejectAttachCcnInstancesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ReleaseAddresses(self, request):
        """本接口 (ReleaseAddresses) 用于释放一个或多个[弹性公网IP](https://cloud.tencent.com/document/product/213/1941)（简称 EIP）。
        * 该操作不可逆，释放后 EIP 关联的 IP 地址将不再属于您的名下。
        * 只有状态为 UNBIND 的 EIP 才能进行释放操作。

        :param request: Request instance for ReleaseAddresses.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ReleaseAddressesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ReleaseAddressesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ReleaseAddresses", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ReleaseAddressesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ReplaceDirectConnectGatewayCcnRoutes(self, request):
        """本接口（ReplaceDirectConnectGatewayCcnRoutes）根据路由ID（RouteId）修改指定的路由（Route），支持批量修改。

        :param request: Request instance for ReplaceDirectConnectGatewayCcnRoutes.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ReplaceDirectConnectGatewayCcnRoutesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ReplaceDirectConnectGatewayCcnRoutesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ReplaceDirectConnectGatewayCcnRoutes", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ReplaceDirectConnectGatewayCcnRoutesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ReplaceRouteTableAssociation(self, request):
        """本接口（ReplaceRouteTableAssociation)用于修改子网（Subnet）关联的路由表（RouteTable）。
        * 一个子网只能关联一个路由表。

        :param request: Request instance for ReplaceRouteTableAssociation.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ReplaceRouteTableAssociationRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ReplaceRouteTableAssociationResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ReplaceRouteTableAssociation", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ReplaceRouteTableAssociationResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ReplaceRoutes(self, request):
        """本接口（ReplaceRoutes）根据路由策略ID（RouteId）修改指定的路由策略（Route），支持批量修改。

        :param request: Request instance for ReplaceRoutes.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ReplaceRoutesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ReplaceRoutesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ReplaceRoutes", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ReplaceRoutesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ReplaceSecurityGroupPolicy(self, request):
        """本接口（ReplaceSecurityGroupPolicy）用于替换单条安全组规则（SecurityGroupPolicy）。
        单个请求中只能替换单个方向的一条规则, 必须要指定索引（PolicyIndex）。

        :param request: Request instance for ReplaceSecurityGroupPolicy.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ReplaceSecurityGroupPolicyRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ReplaceSecurityGroupPolicyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ReplaceSecurityGroupPolicy", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ReplaceSecurityGroupPolicyResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ResetAttachCcnInstances(self, request):
        """本接口（ResetAttachCcnInstances）用于跨账号关联实例申请过期时，重新申请关联操作。

        :param request: Request instance for ResetAttachCcnInstances.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ResetAttachCcnInstancesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ResetAttachCcnInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ResetAttachCcnInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ResetAttachCcnInstancesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ResetNatGatewayConnection(self, request):
        """本接口（ResetNatGatewayConnection）用来NAT网关并发连接上限。

        :param request: Request instance for ResetNatGatewayConnection.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ResetNatGatewayConnectionRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ResetNatGatewayConnectionResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ResetNatGatewayConnection", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ResetNatGatewayConnectionResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ResetRoutes(self, request):
        """本接口（ResetRoutes）用于对某个路由表名称和所有路由策略（Route）进行重新设置。<br />
        注意: 调用本接口是先删除当前路由表中所有路由策略, 再保存新提交的路由策略内容, 会引起网络中断。

        :param request: Request instance for ResetRoutes.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ResetRoutesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ResetRoutesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ResetRoutes", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ResetRoutesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ResetVpnConnection(self, request):
        """本接口(ResetVpnConnection)用于重置VPN通道。

        :param request: Request instance for ResetVpnConnection.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ResetVpnConnectionRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ResetVpnConnectionResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ResetVpnConnection", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ResetVpnConnectionResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ResetVpnGatewayInternetMaxBandwidth(self, request):
        """本接口（ResetVpnGatewayInternetMaxBandwidth）调整VPN网关带宽上限。目前支持升级配置，如果是包年包月VPN网关需要在有效期内。

        :param request: Request instance for ResetVpnGatewayInternetMaxBandwidth.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ResetVpnGatewayInternetMaxBandwidthRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ResetVpnGatewayInternetMaxBandwidthResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ResetVpnGatewayInternetMaxBandwidth", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ResetVpnGatewayInternetMaxBandwidthResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def SetCcnRegionBandwidthLimits(self, request):
        """本接口（SetCcnRegionBandwidthLimits）用于设置云联网（CCN）各地域出带宽上限，该接口只能设置已关联网络实例包含的地域的出带宽上限

        :param request: Request instance for SetCcnRegionBandwidthLimits.
        :type request: :class:`tencentcloud.vpc.v20170312.models.SetCcnRegionBandwidthLimitsRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.SetCcnRegionBandwidthLimitsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("SetCcnRegionBandwidthLimits", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SetCcnRegionBandwidthLimitsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def TransformAddress(self, request):
        """本接口 (TransformAddress) 用于将实例的普通公网 IP 转换为[弹性公网IP](https://cloud.tencent.com/document/product/213/1941)（简称 EIP）。
        * 平台对用户每地域每日解绑 EIP 重新分配普通公网 IP 次数有所限制（可参见 [EIP 产品简介](/document/product/213/1941)）。上述配额可通过 [DescribeAddressQuota](https://cloud.tencent.com/document/api/213/1378) 接口获取。

        :param request: Request instance for TransformAddress.
        :type request: :class:`tencentcloud.vpc.v20170312.models.TransformAddressRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.TransformAddressResponse`

        """
        try:
            params = request._serialize()
            body = self.call("TransformAddress", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.TransformAddressResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def UnassignIpv6Addresses(self, request):
        """本接口（UnassignIpv6Addresses）用于释放弹性网卡`IPv6`地址。<br />
        本接口是异步完成，如需查询异步任务执行结果，请使用本接口返回的`RequestId`轮询`QueryTask`接口。

        :param request: Request instance for UnassignIpv6Addresses.
        :type request: :class:`tencentcloud.vpc.v20170312.models.UnassignIpv6AddressesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.UnassignIpv6AddressesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UnassignIpv6Addresses", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UnassignIpv6AddressesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def UnassignIpv6CidrBlock(self, request):
        """本接口（UnassignIpv6CidrBlock）用于释放IPv6网段。<br />
        网段如果还有IP占用且未回收，则网段无法释放。

        :param request: Request instance for UnassignIpv6CidrBlock.
        :type request: :class:`tencentcloud.vpc.v20170312.models.UnassignIpv6CidrBlockRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.UnassignIpv6CidrBlockResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UnassignIpv6CidrBlock", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UnassignIpv6CidrBlockResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def UnassignIpv6SubnetCidrBlock(self, request):
        """本接口（UnassignIpv6SubnetCidrBlock）用于释放IPv6子网段。<br />
        子网段如果还有IP占用且未回收，则子网段无法释放。

        :param request: Request instance for UnassignIpv6SubnetCidrBlock.
        :type request: :class:`tencentcloud.vpc.v20170312.models.UnassignIpv6SubnetCidrBlockRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.UnassignIpv6SubnetCidrBlockResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UnassignIpv6SubnetCidrBlock", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UnassignIpv6SubnetCidrBlockResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def UnassignPrivateIpAddresses(self, request):
        """本接口（UnassignPrivateIpAddresses）用于弹性网卡退还内网 IP。
        * 退还弹性网卡上的辅助内网IP，接口自动解关联弹性公网 IP。不能退还弹性网卡的主内网IP。

        :param request: Request instance for UnassignPrivateIpAddresses.
        :type request: :class:`tencentcloud.vpc.v20170312.models.UnassignPrivateIpAddressesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.UnassignPrivateIpAddressesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UnassignPrivateIpAddresses", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UnassignPrivateIpAddressesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)