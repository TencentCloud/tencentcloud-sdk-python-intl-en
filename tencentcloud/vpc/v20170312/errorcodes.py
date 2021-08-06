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


# The account quota is reached. Each Tencent Cloud account can create up to 20 EIPs in each region.
ADDRESSQUOTALIMITEXCEEDED = 'AddressQuotaLimitExceeded'

# The maximum number of requests is reached. The maximum number of requests made by a Tencent Cloud account per day in each region equals to two times the quota.
ADDRESSQUOTALIMITEXCEEDED_DAILYALLOCATE = 'AddressQuotaLimitExceeded.DailyAllocate'

# CAM signature or authentication error.
AUTHFAILURE = 'AuthFailure'

# An internal error occurred.
INTERNALERROR = 'InternalError'

# Internal error.
INTERNALSERVERERROR = 'InternalServerError'

# This account is not supported.
INVALIDACCOUNT_NOTSUPPORTED = 'InvalidAccount.NotSupported'

# The specified EIP is in blocked status. When the EIP is in blocked status, it cannot be bound. You must first unblock it.
INVALIDADDRESSID_BLOCKED = 'InvalidAddressId.Blocked'

#  The specified EIP does not exist.
INVALIDADDRESSID_NOTFOUND = 'InvalidAddressId.NotFound'

# The specified EIP is in arrears.
INVALIDADDRESSIDSTATE_INARREARS = 'InvalidAddressIdState.InArrears'

# The specified EIP cannot be bound in current status. It can only be bound in UNBIND status.
INVALIDADDRESSIDSTATUS_NOTPERMIT = 'InvalidAddressIdStatus.NotPermit'

# The operation cannot be performed on the specified EIP in current status.
INVALIDADDRESSSTATE = 'InvalidAddressState'

# This instance is not supported.
INVALIDINSTANCE_NOTSUPPORTED = 'InvalidInstance.NotSupported'

# The specified instance has already been bound to an EIP. You must  unbind the current EIP first before binding another EIP.
INVALIDINSTANCEID_ALREADYBINDEIP = 'InvalidInstanceId.AlreadyBindEip'

# Invalid instance ID. The specified instance ID does not exist.
INVALIDINSTANCEID_NOTFOUND = 'InvalidInstanceId.NotFound'

# The specified NetworkInterfaceId does not exist or the specified PrivateIpAddress is not on the NetworkInterfaceId.
INVALIDNETWORKINTERFACEID_NOTFOUND = 'InvalidNetworkInterfaceId.NotFound'

# A parameter error occurred.
INVALIDPARAMETER = 'InvalidParameter'

# The parameters cannot be specified at the same time.
INVALIDPARAMETER_COEXIST = 'InvalidParameter.Coexist'

# The specified filter condition does not exist.
INVALIDPARAMETER_FILTERINVALIDKEY = 'InvalidParameter.FilterInvalidKey'

# The specified filter condition should be a key-value pair.
INVALIDPARAMETER_FILTERNOTDICT = 'InvalidParameter.FilterNotDict'

# The specified filter value should be a list.
INVALIDPARAMETER_FILTERVALUESNOTLIST = 'InvalidParameter.FilterValuesNotList'

# The next hop type does not match with the next hop gateway.
INVALIDPARAMETER_NEXTHOPMISMATCH = 'InvalidParameter.NextHopMismatch'

# The two parameters cannot be specified at the same time, nor exist concurrently. EIP can only be bound to the instances or the specified private IPs of the specified ENIs.
INVALIDPARAMETERCONFLICT = 'InvalidParameterConflict'

# Incorrect parameter value.
INVALIDPARAMETERVALUE = 'InvalidParameterValue'

# The bandwidth exceeds the limit.
INVALIDPARAMETERVALUE_BANDWIDTHOUTOFRANGE = 'InvalidParameterValue.BandwidthOutOfRange'

# The selected bandwidth is smaller than the minimum permissible range.
INVALIDPARAMETERVALUE_BANDWIDTHTOOSMALL = 'InvalidParameterValue.BandwidthTooSmall'

# The number of BM VPCs associated with the specified CCN has reached the upper limit.
INVALIDPARAMETERVALUE_CCNATTACHBMVPCLIMITEXCEEDED = 'InvalidParameterValue.CcnAttachBmvpcLimitExceeded'

# The destination IP address range is not within the CIDR range of the the customer VPC.
INVALIDPARAMETERVALUE_CIDRNOTINPEERVPC = 'InvalidParameterValue.CidrNotInPeerVpc'

# Invalid input parameters
INVALIDPARAMETERVALUE_COMBINATION = 'InvalidParameterValue.Combination'

# The input parameter already exists.
INVALIDPARAMETERVALUE_DUPLICATE = 'InvalidParameterValue.Duplicate'

# Missing parameters.
INVALIDPARAMETERVALUE_EMPTY = 'InvalidParameterValue.Empty'

# Invalid DedicatedClusterId.
INVALIDPARAMETERVALUE_INVALIDDEDICATEDCLUSTERID = 'InvalidParameterValue.InvalidDedicatedClusterId'

# The parameter value exceeds the limit.
INVALIDPARAMETERVALUE_LIMITEXCEEDED = 'InvalidParameterValue.LimitExceeded'

# Invalid input parameter format.
INVALIDPARAMETERVALUE_MALFORMED = 'InvalidParameterValue.Malformed'

# The NAT Gateway already has an identical SNAT rule.
INVALIDPARAMETERVALUE_NATSNATRULEEXISTS = 'InvalidParameterValue.NatSnatRuleExists'

# The detection destination IP address is the same as that of another network detection instance under the same subnet in the same VPC.
INVALIDPARAMETERVALUE_NETDETECTSAMEIP = 'InvalidParameterValue.NetDetectSameIp'

# This operation is only available for primary ENIs.
INVALIDPARAMETERVALUE_ONLYSUPPORTEDFORMASTERNETWORKCARD = 'InvalidParameterValue.OnlySupportedForMasterNetworkCard'

# The parameter value is not in the specified range.
INVALIDPARAMETERVALUE_RANGE = 'InvalidParameterValue.Range'

# The parameter value is retained by the system.
INVALIDPARAMETERVALUE_RESERVED = 'InvalidParameterValue.Reserved'

# Subnet CIDR conflict.
INVALIDPARAMETERVALUE_SUBNETCONFLICT = 'InvalidParameterValue.SubnetConflict'

# Invalid subnet CIDR.
INVALIDPARAMETERVALUE_SUBNETRANGE = 'InvalidParameterValue.SubnetRange'

# Invalid parameter value. The parameter value is too long.
INVALIDPARAMETERVALUE_TOOLONG = 'InvalidParameterValue.TooLong'

# Destination IP address range conflicts with CIDR of the current VPC.
INVALIDPARAMETERVALUE_VPCCIDRCONFLICT = 'InvalidParameterValue.VpcCidrConflict'

# Destination IP address range conflicts with CIDR block of the current VPC tunnel.
INVALIDPARAMETERVALUE_VPNCONNCIDRCONFLICT = 'InvalidParameterValue.VpnConnCidrConflict'

# The `Zone` parameter value should be the zone where CDC resides.
INVALIDPARAMETERVALUE_ZONECONFLICT = 'InvalidParameterValue.ZoneConflict'

# The specified private IP of the specified ENI has already been bound to an EIP. A private IP cannot be bound to more than one EIP.
INVALIDPRIVATEIPADDRESS_ALREADYBINDEIP = 'InvalidPrivateIpAddress.AlreadyBindEip'

# Invalid routing policy ID (RouteId).
INVALIDROUTEID_NOTFOUND = 'InvalidRouteId.NotFound'

# Invalid route table. The route table ID is invalid.
INVALIDROUTETABLEID_MALFORMED = 'InvalidRouteTableId.Malformed'

# Invalid route table. The VPC resource does not exist. Please check and enter the correct resource information.
INVALIDROUTETABLEID_NOTFOUND = 'InvalidRouteTableId.NotFound'

# Invalid security group. The security group instance ID is invalid.
INVALIDSECURITYGROUPID_MALFORMED = 'InvalidSecurityGroupID.Malformed'

# Invalid security group. The security group instance ID does not exist.
INVALIDSECURITYGROUPID_NOTFOUND = 'InvalidSecurityGroupID.NotFound'

# Invalid VPC. The VPC instance ID is invalid.
INVALIDVPCID_MALFORMED = 'InvalidVpcId.Malformed'

# Invalid VPC. The VPC resource does not exist.
INVALIDVPCID_NOTFOUND = 'InvalidVpcId.NotFound'

# Invalid VPN gateway. The VPN instance ID is invalid.
INVALIDVPNGATEWAYID_MALFORMED = 'InvalidVpnGatewayId.Malformed'

# Invalid VPN gateway. The VPN instance does not exist. Verify if you have entered the correct resource information.
INVALIDVPNGATEWAYID_NOTFOUND = 'InvalidVpnGatewayId.NotFound'

# Quota limit is reached.
LIMITEXCEEDED = 'LimitExceeded'

# The number of assigned IP addresses has reached the upper limit.
LIMITEXCEEDED_ADDRESS = 'LimitExceeded.Address'

# The number of EIPs applied for exceeds the upper limit.
LIMITEXCEEDED_ADDRESSQUOTALIMITEXCEEDED = 'LimitExceeded.AddressQuotaLimitExceeded'

# The number of assigned IP ranges of the VPC has reached the upper limit.
LIMITEXCEEDED_CIDRBLOCK = 'LimitExceeded.CidrBlock'

# The number of EIPs applied for exceeds the daily upper limit.
LIMITEXCEEDED_DAILYALLOCATEADDRESSQUOTALIMITEXCEEDED = 'LimitExceeded.DailyAllocateAddressQuotaLimitExceeded'

# The number of NAT gateways created by the VPC has reached the upper limit.
LIMITEXCEEDED_NATGATEWAYPERVPCLIMITEXCEEDED = 'LimitExceeded.NatGatewayPerVpcLimitExceeded'

# The number of EIPs bound to the NAT gateway has reached the upper limit.
LIMITEXCEEDED_PUBLICIPADDRESSPERNATGATEWAYLIMITEXCEEDED = 'LimitExceeded.PublicIpAddressPerNatGatewayLimitExceeded'

# The number of security group rules exceeds the upper limit.
LIMITEXCEEDED_SECURITYGROUPPOLICYSET = 'LimitExceeded.SecurityGroupPolicySet'

# The number of subnet IP ranges assigned in the subnet has reached the upper limit.
LIMITEXCEEDED_SUBNETCIDRBLOCK = 'LimitExceeded.SubnetCidrBlock'

# Missing parameter.
MISSINGPARAMETER = 'MissingParameter'

# The resource is occupied.
RESOURCEINUSE = 'ResourceInUse'

# The specified IP address is already in use.
RESOURCEINUSE_ADDRESS = 'ResourceInUse.Address'

# Insufficient resources.
RESOURCEINSUFFICIENT = 'ResourceInsufficient'

# The IP range resources are insufficient.
RESOURCEINSUFFICIENT_CIDRBLOCK = 'ResourceInsufficient.CidrBlock'

# The resource does not exist.
RESOURCENOTFOUND = 'ResourceNotFound'

# The resource is unavailable.
RESOURCEUNAVAILABLE = 'ResourceUnavailable'

# Unauthorized operation.
UNAUTHORIZEDOPERATION = 'UnauthorizedOperation'

# The binding relationship does not exist.
UNAUTHORIZEDOPERATION_ATTACHMENTNOTFOUND = 'UnauthorizedOperation.AttachmentNotFound'

# Identity verification has not been completed for the account.
UNAUTHORIZEDOPERATION_NOREALNAMEAUTHENTICATION = 'UnauthorizedOperation.NoRealNameAuthentication'

# The operation is not allowed for a primary IP.
UNAUTHORIZEDOPERATION_PRIMARYIP = 'UnauthorizedOperation.PrimaryIp'

# Unknown parameter error.
UNKNOWNPARAMETER = 'UnknownParameter'

# Unknown parameter. Try similar parameters.
UNKNOWNPARAMETER_WITHGUESS = 'UnknownParameter.WithGuess'

# Unsupported operation.
UNSUPPORTEDOPERATION = 'UnsupportedOperation'

# The port does not exist.
UNSUPPORTEDOPERATION_ACTIONNOTFOUND = 'UnsupportedOperation.ActionNotFound'

# The EIP is already bound to a CVM.
UNSUPPORTEDOPERATION_ATTACHMENTALREADYEXISTS = 'UnsupportedOperation.AttachmentAlreadyExists'

# The binding relationship does not exist.
UNSUPPORTEDOPERATION_ATTACHMENTNOTFOUND = 'UnsupportedOperation.AttachmentNotFound'

# Unable to delete the current CCN instance: its monthly-subscribed bandwidth does not expire. 
UNSUPPORTEDOPERATION_BANDWIDTHNOTEXPIRED = 'UnsupportedOperation.BandwidthNotExpired'

# EIP has already been bound.
UNSUPPORTEDOPERATION_BINDEIP = 'UnsupportedOperation.BindEIP'

# The specified VPC CIDR range does not support Classiclink.
UNSUPPORTEDOPERATION_CIDRUNSUPPORTEDCLASSICLINK = 'UnsupportedOperation.CIDRUnSupportedClassicLink'

# The instance is already associated with a CCN.
UNSUPPORTEDOPERATION_CCNATTACHED = 'UnsupportedOperation.CcnAttached'

# The instance is not associated with a CCN.
UNSUPPORTEDOPERATION_CCNNOTATTACHED = 'UnsupportedOperation.CcnNotAttached'

# The specified route table does not exist.
UNSUPPORTEDOPERATION_CCNROUTETABLENOTEXIST = 'UnsupportedOperation.CcnRouteTableNotExist'

# CDC subnet can only create a route to the local gateway.
UNSUPPORTEDOPERATION_CDCSUBNETNOTSUPPORTUNLOCALGATEWAY = 'UnsupportedOperation.CdcSubnetNotSupportUnLocalGateway'

# The instance has already been bound to the VPC.
UNSUPPORTEDOPERATION_CLASSICINSTANCEIDALREADYEXISTS = 'UnsupportedOperation.ClassicInstanceIdAlreadyExists'

# Public network CLB does not support this policy.
UNSUPPORTEDOPERATION_CLBPOLICYLIMIT = 'UnsupportedOperation.ClbPolicyLimit'

# The IP range overlaps with that of the TKE container under the VPC.
UNSUPPORTEDOPERATION_CONFLICTWITHDOCKERROUTE = 'UnsupportedOperation.ConflictWithDockerRoute'

# No direct connect gateway exists in the specified VPC.
UNSUPPORTEDOPERATION_DCGATEWAYSNOTFOUNDINVPC = 'UnsupportedOperation.DcGatewaysNotFoundInVpc'

# Direct connect gateway is updating the BGP Community attribute.
UNSUPPORTEDOPERATION_DIRECTCONNECTGATEWAYISUPDATINGCOMMUNITY = 'UnsupportedOperation.DirectConnectGatewayIsUpdatingCommunity'

# The specified routing policy cannot be re-published to CCN. Please first withdraw it from CCN.
UNSUPPORTEDOPERATION_DISABLEDNOTIFYCCN = 'UnsupportedOperation.DisabledNotifyCcn'

# The security group policies are repeated.
UNSUPPORTEDOPERATION_DUPLICATEPOLICY = 'UnsupportedOperation.DuplicatePolicy'

# ECMP is not supported.
UNSUPPORTEDOPERATION_ECMP = 'UnsupportedOperation.Ecmp'

# Form an ECMP with the CCN route.
UNSUPPORTEDOPERATION_ECMPWITHCCNROUTE = 'UnsupportedOperation.EcmpWithCcnRoute'

# Form an ECMP with the user’s custom routes.
UNSUPPORTEDOPERATION_ECMPWITHUSERROUTE = 'UnsupportedOperation.EcmpWithUserRoute'

# The configured instance does not match with the route table.
UNSUPPORTEDOPERATION_INSTANCEANDRTBNOTMATCH = 'UnsupportedOperation.InstanceAndRtbNotMatch'

# Insufficient account balance.
UNSUPPORTEDOPERATION_INSUFFICIENTFUNDS = 'UnsupportedOperation.InsufficientFunds'

# Invalid instance status.
UNSUPPORTEDOPERATION_INVALIDINSTANCESTATE = 'UnsupportedOperation.InvalidInstanceState'

# Invalid resource status.
UNSUPPORTEDOPERATION_INVALIDSTATE = 'UnsupportedOperation.InvalidState'

# The account of the instance associated with the current CCN is not a Financial Cloud account.
UNSUPPORTEDOPERATION_ISNOTFINANCEACCOUNT = 'UnsupportedOperation.IsNotFinanceAccount'

# The specified CDC instance already has a local gateway.
UNSUPPORTEDOPERATION_LOCALGATEWAYALREADYEXISTS = 'UnsupportedOperation.LocalGateWayAlreadyExists'

# The resource mutual exclusion operation is being executed.
UNSUPPORTEDOPERATION_MUTEXOPERATIONTASKRUNNING = 'UnsupportedOperation.MutexOperationTaskRunning'

# The specified NAT Gateway type does not support configuring a SNAT rule.
UNSUPPORTEDOPERATION_NATGATEWAYTYPENOTSUPPORTSNAT = 'UnsupportedOperation.NatGatewayTypeNotSupportSNAT'

# The specified subnet does not support creating a route to the local gateway.
UNSUPPORTEDOPERATION_NORMALSUBNETNOTSUPPORTLOCALGATEWAY = 'UnsupportedOperation.NormalSubnetNotSupportLocalGateway'

# Unsupported operation: the current CCN instance is not in “Applying” status.
UNSUPPORTEDOPERATION_NOTPENDINGCCNINSTANCE = 'UnsupportedOperation.NotPendingCcnInstance'

# Unsupported operation: the current CCN instance is not billed on a pay-as-you-go basis.
UNSUPPORTEDOPERATION_NOTPOSTPAIDCCNOPERATION = 'UnsupportedOperation.NotPostpaidCcnOperation'

# The specified routing policy cannot be published to or withdrawn from CCN.
UNSUPPORTEDOPERATION_NOTIFYCCN = 'UnsupportedOperation.NotifyCcn'

# The monthly subscription CCN instance only supports the inter-region bandwidth limit.
UNSUPPORTEDOPERATION_PREPAIDCCNONLYSUPPORTINTERREGIONLIMIT = 'UnsupportedOperation.PrepaidCcnOnlySupportInterRegionLimit'

# The specified value is a primary IP.
UNSUPPORTEDOPERATION_PRIMARYIP = 'UnsupportedOperation.PrimaryIp'

# At least one EIP exists on the NAT gateway, and the EIP cannot be unbound.
UNSUPPORTEDOPERATION_PUBLICIPADDRESSDISASSOCIATE = 'UnsupportedOperation.PublicIpAddressDisassociate'

# The EIP bound to the NAT gateway is not a BGP IP.
UNSUPPORTEDOPERATION_PUBLICIPADDRESSISNOTBGPIP = 'UnsupportedOperation.PublicIpAddressIsNotBGPIp'

# The EIP bound to the NAT gateway does not exist.
UNSUPPORTEDOPERATION_PUBLICIPADDRESSISNOTEXISTED = 'UnsupportedOperation.PublicIpAddressIsNotExisted'

# The EIP bound to the NAT gateway is not bill-by-traffic.
UNSUPPORTEDOPERATION_PUBLICIPADDRESSNOTBILLEDBYTRAFFIC = 'UnsupportedOperation.PublicIpAddressNotBilledByTraffic'

# The resource ID entered does not match with any resource bound with the IP. Check and try again.
UNSUPPORTEDOPERATION_RESOURCEMISMATCH = 'UnsupportedOperation.ResourceMismatch'

# The endpoint created by the specified endpoint service cannot be bound to a security group.
UNSUPPORTEDOPERATION_SPECIALENDPOINTSERVICE = 'UnsupportedOperation.SpecialEndPointService'

# System route. Operation is prohibited.
UNSUPPORTEDOPERATION_SYSTEMROUTE = 'UnsupportedOperation.SystemRoute'

# The account ID does not exist.
UNSUPPORTEDOPERATION_UINNOTFOUND = 'UnsupportedOperation.UinNotFound'

# Cross border is not supported.
UNSUPPORTEDOPERATION_UNABLECROSSBORDER = 'UnsupportedOperation.UnableCrossBorder'

# The current CCN cannot be associated with a Financial Cloud instance.
UNSUPPORTEDOPERATION_UNABLECROSSFINANCE = 'UnsupportedOperation.UnableCrossFinance'

# IPv6 IP range is not assigned.
UNSUPPORTEDOPERATION_UNASSIGNCIDRBLOCK = 'UnsupportedOperation.UnassignCidrBlock'

# EIP is not bound.
UNSUPPORTEDOPERATION_UNBINDEIP = 'UnsupportedOperation.UnbindEIP'

# The specified instance type does not support ENIs.
UNSUPPORTEDOPERATION_UNSUPPORTEDINSTANCEFAMILY = 'UnsupportedOperation.UnsupportedInstanceFamily'

# The selected CCN instance cannot be created because the payment type is not supported.
UNSUPPORTEDOPERATION_USERANDCCNCHARGETYPENOTMATCH = 'UnsupportedOperation.UserAndCcnChargeTypeNotMatch'

# The specified version number of the security group policy is inconsistent with the latest version.
UNSUPPORTEDOPERATION_VERSIONMISMATCH = 'UnsupportedOperation.VersionMismatch'

# The resources are not in the same VPC.
UNSUPPORTEDOPERATION_VPCMISMATCH = 'UnsupportedOperation.VpcMismatch'

# The specified resources are not in the same availability zone.
UNSUPPORTEDOPERATION_ZONEMISMATCH = 'UnsupportedOperation.ZoneMismatch'

# The maximum number of VPC resource requests for the specified region has been reached.
VPCLIMITEXCEEDED = 'VpcLimitExceeded'
