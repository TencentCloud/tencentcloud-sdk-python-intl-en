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

# The ENI information is not available in this address.
FAILEDOPERATION_ADDRESSENIINFONOTFOUND = 'FailedOperation.AddressEniInfoNotFound'

# Insufficient account balance.
FAILEDOPERATION_BALANCEINSUFFICIENT = 'FailedOperation.BalanceInsufficient'

# Unsupported region.
FAILEDOPERATION_INVALIDREGION = 'FailedOperation.InvalidRegion'

# The instance's primary ENI is not found.
FAILEDOPERATION_MASTERENINOTFOUND = 'FailedOperation.MasterEniNotFound'

# Network probe timed out. Please retry later.
FAILEDOPERATION_NETDETECTTIMEOUT = 'FailedOperation.NetDetectTimeOut'

# Task execution failed.
FAILEDOPERATION_TASKFAILED = 'FailedOperation.TaskFailed'

# An internal error occurred.
INTERNALERROR = 'InternalError'

# Failed to create the Ckafka route. Please retry later.
INTERNALERROR_CREATECKAFKAROUTEERROR = 'InternalError.CreateCkafkaRouteError'

# Internal module error
INTERNALERROR_MODULEERROR = 'InternalError.ModuleError'

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

# 
INVALIDPARAMETER_ACLTYPEMISMATCH = 'InvalidParameter.AclTypeMismatch'

# The parameters cannot be specified at the same time.
INVALIDPARAMETER_COEXIST = 'InvalidParameter.Coexist'

# The specified filter condition does not exist.
INVALIDPARAMETER_FILTERINVALIDKEY = 'InvalidParameter.FilterInvalidKey'

# The specified filter condition should be a key-value pair.
INVALIDPARAMETER_FILTERNOTDICT = 'InvalidParameter.FilterNotDict'

# The specified filter value should be a list.
INVALIDPARAMETER_FILTERVALUESNOTLIST = 'InvalidParameter.FilterValuesNotList'

# The filter rule is invalid.
INVALIDPARAMETER_INVALIDFILTER = 'InvalidParameter.InvalidFilter'

# The next hop type does not match with the next hop gateway.
INVALIDPARAMETER_NEXTHOPMISMATCH = 'InvalidParameter.NextHopMismatch'

# The cross-AZ placement group of the DC gateway doesn't exist.
INVALIDPARAMETER_VPGHAGROUPNOTFOUND = 'InvalidParameter.VpgHaGroupNotFound'

# The two parameters cannot be specified at the same time, nor exist concurrently. EIP can only be bound to the instances or the specified private IPs of the specified ENIs.
INVALIDPARAMETERCONFLICT = 'InvalidParameterConflict'

# Incorrect parameter value.
INVALIDPARAMETERVALUE = 'InvalidParameterValue'

# Attacked IP address.
INVALIDPARAMETERVALUE_ADDRESSATTACKED = 'InvalidParameterValue.AddressAttacked'

# This IP address ID is invalid.
INVALIDPARAMETERVALUE_ADDRESSIDMALFORMED = 'InvalidParameterValue.AddressIdMalformed'

# The billing mode of this IP address conflicts with that of other IP addresses.
INVALIDPARAMETERVALUE_ADDRESSINTERNETCHARGETYPECONFLICT = 'InvalidParameterValue.AddressInternetChargeTypeConflict'

# The IP address is not available now.
INVALIDPARAMETERVALUE_ADDRESSIPNOTAVAILABLE = 'InvalidParameterValue.AddressIpNotAvailable'

# Failed to query the address.
INVALIDPARAMETERVALUE_ADDRESSIPSNOTFOUND = 'InvalidParameterValue.AddressIpsNotFound'

# An EIP cannot be bound with this type of instance.
INVALIDPARAMETERVALUE_ADDRESSNOTAPPLICABLE = 'InvalidParameterValue.AddressNotApplicable'

# This IP address is not a CalcIP (device IP).
INVALIDPARAMETERVALUE_ADDRESSNOTCALCIP = 'InvalidParameterValue.AddressNotCalcIP'

# Unable to find the address.
INVALIDPARAMETERVALUE_ADDRESSNOTFOUND = 'InvalidParameterValue.AddressNotFound'

# 
INVALIDPARAMETERVALUE_ADDRESSTYPECONFLICT = 'InvalidParameterValue.AddressTypeConflict'

# The bandwidth exceeds the limit.
INVALIDPARAMETERVALUE_BANDWIDTHOUTOFRANGE = 'InvalidParameterValue.BandwidthOutOfRange'

# Incorrect bandwidth package ID.
INVALIDPARAMETERVALUE_BANDWIDTHPACKAGEIDMALFORMED = 'InvalidParameterValue.BandwidthPackageIdMalformed'

# The bandwidth package is in use.
INVALIDPARAMETERVALUE_BANDWIDTHPACKAGEINUSE = 'InvalidParameterValue.BandwidthPackageInUse'

# Failed to query the bandwidth package
INVALIDPARAMETERVALUE_BANDWIDTHPACKAGENOTFOUND = 'InvalidParameterValue.BandwidthPackageNotFound'

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

# The parameter value already exists.
INVALIDPARAMETERVALUE_DUPLICATEPARA = 'InvalidParameterValue.DuplicatePara'

# Exceeded the upper limit.
INVALIDPARAMETERVALUE_EIPBRANDWIDTHOUTINVALID = 'InvalidParameterValue.EIPBrandWidthOutInvalid'

# Missing parameters.
INVALIDPARAMETERVALUE_EMPTY = 'InvalidParameterValue.Empty'

# The billing mode of this instance is different from that of others.
INVALIDPARAMETERVALUE_INCONSISTENTINSTANCEINTERNETCHARGETYPE = 'InvalidParameterValue.InconsistentInstanceInternetChargeType'

# This instance does not support an Anycast EIP.
INVALIDPARAMETERVALUE_INSTANCEDOESNOTSUPPORTANYCAST = 'InvalidParameterValue.InstanceDoesNotSupportAnycast'

# The instance does not have a public IP.
INVALIDPARAMETERVALUE_INSTANCEHASNOWANIP = 'InvalidParameterValue.InstanceHasNoWanIP'

# This instance already has a WanIP (public IP).
INVALIDPARAMETERVALUE_INSTANCEHASWANIP = 'InvalidParameterValue.InstanceHasWanIP'

# Incorrect instance ID.
INVALIDPARAMETERVALUE_INSTANCEIDMALFORMED = 'InvalidParameterValue.InstanceIdMalformed'

# Request failed: this instance does not have a CalcIP (device IP).
INVALIDPARAMETERVALUE_INSTANCENOCALCIP = 'InvalidParameterValue.InstanceNoCalcIP'

# Request failed: this instance does not have a WanIP (public IP).
INVALIDPARAMETERVALUE_INSTANCENOWANIP = 'InvalidParameterValue.InstanceNoWanIP'

# Failed to bind: this IP is restricted
INVALIDPARAMETERVALUE_INSTANCENORMALPUBLICIPBLOCKED = 'InvalidParameterValue.InstanceNormalPublicIpBlocked'

# The ENI and the IP are bound with different instances.
INVALIDPARAMETERVALUE_INSTANCENOTMATCHASSOCIATEENI = 'InvalidParameterValue.InstanceNotMatchAssociateEni'

# The network billing mode has not been changed.
INVALIDPARAMETERVALUE_INTERNETCHARGETYPENOTCHANGED = 'InvalidParameterValue.InternetChargeTypeNotChanged'

# Invalid billing mode of bandwidth package
INVALIDPARAMETERVALUE_INVALIDBANDWIDTHPACKAGECHARGETYPE = 'InvalidParameterValue.InvalidBandwidthPackageChargeType'

# The parameter value does not exist or is not supported.
INVALIDPARAMETERVALUE_INVALIDBUSINESS = 'InvalidParameterValue.InvalidBusiness'

# Invalid DedicatedClusterId.
INVALIDPARAMETERVALUE_INVALIDDEDICATEDCLUSTERID = 'InvalidParameterValue.InvalidDedicatedClusterId'

# This IP is applicable only for pay-as-you-go instances that billed by hourly traffic and instances with bandwidth package.
INVALIDPARAMETERVALUE_INVALIDINSTANCEINTERNETCHARGETYPE = 'InvalidParameterValue.InvalidInstanceInternetChargeType'

# Operation failed: the status of the instance does not allow this operation.
INVALIDPARAMETERVALUE_INVALIDINSTANCESTATE = 'InvalidParameterValue.InvalidInstanceState'

# This Tag is invalid.
INVALIDPARAMETERVALUE_INVALIDTAG = 'InvalidParameterValue.InvalidTag'

# This CLB instance is already bound with an EIP.
INVALIDPARAMETERVALUE_LBALREADYBINDEIP = 'InvalidParameterValue.LBAlreadyBindEip'

# The parameter value exceeds the limit.
INVALIDPARAMETERVALUE_LIMITEXCEEDED = 'InvalidParameterValue.LimitExceeded'

# Invalid input parameter format.
INVALIDPARAMETERVALUE_MALFORMED = 'InvalidParameterValue.Malformed'

# 
INVALIDPARAMETERVALUE_MEMBERAPPROVALAPPLICATIONIDMISMATCH = 'InvalidParameterValue.MemberApprovalApplicationIdMismatch'

# 
INVALIDPARAMETERVALUE_MEMBERAPPROVALAPPLICATIONNOTAPPROVED = 'InvalidParameterValue.MemberApprovalApplicationNotApproved'

# 
INVALIDPARAMETERVALUE_MEMBERAPPROVALAPPLICATIONREJECTED = 'InvalidParameterValue.MemberApprovalApplicationRejected'

# 
INVALIDPARAMETERVALUE_MEMBERAPPROVALAPPLICATIONSTARTED = 'InvalidParameterValue.MemberApprovalApplicationStarted'

# The bound instance is missing.
INVALIDPARAMETERVALUE_MISSINGASSOCIATEENTITY = 'InvalidParameterValue.MissingAssociateEntity'

# A request cannot contain IP addresses with different cluster types.
INVALIDPARAMETERVALUE_MIXEDADDRESSIPSETTYPE = 'InvalidParameterValue.MixedAddressIpSetType'

# The DNAT forwarding rule of the NAT gateway already exists.
INVALIDPARAMETERVALUE_NATGATEWAYDNATRULEEXISTED = 'InvalidParameterValue.NatGatewayDnatRuleExisted'

# The DNAT forwarding rule of the NAT gateway does not exist.
INVALIDPARAMETERVALUE_NATGATEWAYDNATRULENOTEXISTS = 'InvalidParameterValue.NatGatewayDnatRuleNotExists'

# The private IP of the DNAT translation rule must be an IP used by the ENI of the virtual machine.
INVALIDPARAMETERVALUE_NATGATEWAYDNATRULEPIPNEEDVM = 'InvalidParameterValue.NatGatewayDnatRulePipNeedVm'

# The DNAT rule of the NAT gateway to add already exists.
INVALIDPARAMETERVALUE_NATGATEWAYDNATRULEREPEATED = 'InvalidParameterValue.NatGatewayDnatRuleRepeated'

# The SNAT forwarding rule of the NAT gateway does not exist.
INVALIDPARAMETERVALUE_NATGATEWAYSNATRULENOTEXISTS = 'InvalidParameterValue.NatGatewaySnatRuleNotExists'

# The NAT Gateway already has an identical SNAT rule.
INVALIDPARAMETERVALUE_NATSNATRULEEXISTS = 'InvalidParameterValue.NatSnatRuleExists'

# The probe destination IP and network probe are in the same VPC.
INVALIDPARAMETERVALUE_NETDETECTINVPC = 'InvalidParameterValue.NetDetectInVpc'

# Unable to find the matched next hop in the CCN route table for the destination IP.
INVALIDPARAMETERVALUE_NETDETECTNOTFOUNDIP = 'InvalidParameterValue.NetDetectNotFoundIp'

# The detection destination IP address is the same as that of another network detection instance under the same subnet in the same VPC.
INVALIDPARAMETERVALUE_NETDETECTSAMEIP = 'InvalidParameterValue.NetDetectSameIp'

# Incorrect network interface ID.
INVALIDPARAMETERVALUE_NETWORKINTERFACEIDMALFORMED = 'InvalidParameterValue.NetworkInterfaceIdMalformed'

# The network interface ID was not found. The private IP address may not be configured on the network interface.
INVALIDPARAMETERVALUE_NETWORKINTERFACENOTFOUND = 'InvalidParameterValue.NetworkInterfaceNotFound'

# This operation is only available for primary ENIs.
INVALIDPARAMETERVALUE_ONLYSUPPORTEDFORMASTERNETWORKCARD = 'InvalidParameterValue.OnlySupportedForMasterNetworkCard'

# Invalid parameter format
INVALIDPARAMETERVALUE_PARAMETERMISMATCH = 'InvalidParameterValue.ParameterMismatch'

# The parameter value is not in the specified range.
INVALIDPARAMETERVALUE_RANGE = 'InvalidParameterValue.Range'

# The parameter value is retained by the system.
INVALIDPARAMETERVALUE_RESERVED = 'InvalidParameterValue.Reserved'

# The resource has already added to another bandwidth package.
INVALIDPARAMETERVALUE_RESOURCEALREADYEXISTED = 'InvalidParameterValue.ResourceAlreadyExisted'

# The resource has expired.
INVALIDPARAMETERVALUE_RESOURCEEXPIRED = 'InvalidParameterValue.ResourceExpired'

# The resource ID is incorrect.
INVALIDPARAMETERVALUE_RESOURCEIDMALFORMED = 'InvalidParameterValue.ResourceIdMalformed'

# The resource is not associated with this bandwidth package. 
INVALIDPARAMETERVALUE_RESOURCENOTEXISTED = 'InvalidParameterValue.ResourceNotExisted'

# This resource is not found.
INVALIDPARAMETERVALUE_RESOURCENOTFOUND = 'InvalidParameterValue.ResourceNotFound'

# The resource does not support this operation.
INVALIDPARAMETERVALUE_RESOURCENOTSUPPORT = 'InvalidParameterValue.ResourceNotSupport'

# 
INVALIDPARAMETERVALUE_STOPCHARGINGINSTANCEINUSE = 'InvalidParameterValue.StopChargingInstanceInUse'

# Subnet CIDR conflict.
INVALIDPARAMETERVALUE_SUBNETCONFLICT = 'InvalidParameterValue.SubnetConflict'

# The CIDR block overlaps with another subnet within the same VPC.
INVALIDPARAMETERVALUE_SUBNETOVERLAP = 'InvalidParameterValue.SubnetOverlap'

# The subnet IP range overlaps with the secondary CIDR block.
INVALIDPARAMETERVALUE_SUBNETOVERLAPASSISTCIDR = 'InvalidParameterValue.SubnetOverlapAssistCidr'

# Invalid subnet CIDR.
INVALIDPARAMETERVALUE_SUBNETRANGE = 'InvalidParameterValue.SubnetRange'

# Duplicate tag keys.
INVALIDPARAMETERVALUE_TAGDUPLICATEKEY = 'InvalidParameterValue.TagDuplicateKey'

# Duplicate tag resource type.
INVALIDPARAMETERVALUE_TAGDUPLICATERESOURCETYPE = 'InvalidParameterValue.TagDuplicateResourceType'

# Invalid tag key.
INVALIDPARAMETERVALUE_TAGINVALIDKEY = 'InvalidParameterValue.TagInvalidKey'

# Invalid tag key length.
INVALIDPARAMETERVALUE_TAGINVALIDKEYLEN = 'InvalidParameterValue.TagInvalidKeyLen'

# Invalid tag key.
INVALIDPARAMETERVALUE_TAGINVALIDVAL = 'InvalidParameterValue.TagInvalidVal'

# The tag key does not exist.
INVALIDPARAMETERVALUE_TAGKEYNOTEXISTS = 'InvalidParameterValue.TagKeyNotExists'

# Tags are not assigned quotas.
INVALIDPARAMETERVALUE_TAGNOTALLOCATEDQUOTA = 'InvalidParameterValue.TagNotAllocatedQuota'

# The tag and value do not exist.
INVALIDPARAMETERVALUE_TAGNOTEXISTED = 'InvalidParameterValue.TagNotExisted'

# Unsupported tag.
INVALIDPARAMETERVALUE_TAGNOTSUPPORTTAG = 'InvalidParameterValue.TagNotSupportTag'

# 'The tag resource format error.
INVALIDPARAMETERVALUE_TAGRESOURCEFORMATERROR = 'InvalidParameterValue.TagResourceFormatError'

# Exceeded the quota of tag timestamp.
INVALIDPARAMETERVALUE_TAGTIMESTAMPEXCEEDED = 'InvalidParameterValue.TagTimestampExceeded'

# The tag value does not exist.
INVALIDPARAMETERVALUE_TAGVALNOTEXISTS = 'InvalidParameterValue.TagValNotExists'

# Invalid parameter value. The parameter value is too long.
INVALIDPARAMETERVALUE_TOOLONG = 'InvalidParameterValue.TooLong'

# The traffic package ID is invalid.
INVALIDPARAMETERVALUE_TRAFFICPACKAGEIDMALFORMED = 'InvalidParameterValue.TrafficPackageIdMalformed'

# This availability zone is unavailable.
INVALIDPARAMETERVALUE_UNAVAILABLEZONE = 'InvalidParameterValue.UnavailableZone'

# Destination IP address range conflicts with CIDR of the current VPC.
INVALIDPARAMETERVALUE_VPCCIDRCONFLICT = 'InvalidParameterValue.VpcCidrConflict'

# This feature is not available for this direct connect gateway.
INVALIDPARAMETERVALUE_VPGTYPENOTMATCH = 'InvalidParameterValue.VpgTypeNotMatch'

# Destination IP address range conflicts with CIDR block of the current VPC tunnel.
INVALIDPARAMETERVALUE_VPNCONNCIDRCONFLICT = 'InvalidParameterValue.VpnConnCidrConflict'

# The destination IP of the probe cannot be within the IP range of the VPC.
INVALIDPARAMETERVALUE_VPNCONNHEALTHCHECKIPCONFLICT = 'InvalidParameterValue.VpnConnHealthCheckIpConflict'

# The `Zone` parameter value should be the zone where CDC resides.
INVALIDPARAMETERVALUE_ZONECONFLICT = 'InvalidParameterValue.ZoneConflict'

# The specified private IP of the specified ENI has already been bound to an EIP. A private IP cannot be bound to more than one EIP.
INVALIDPRIVATEIPADDRESS_ALREADYBINDEIP = 'InvalidPrivateIpAddress.AlreadyBindEip'

# Invalid RouteId.
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

# Ran out of the quota for returning under this account.
LIMITEXCEEDED_ACCOUNTRETURNQUOTA = 'LimitExceeded.AccountReturnQuota'

# Too often API invocations
LIMITEXCEEDED_ACTIONLIMITED = 'LimitExceeded.ActionLimited'

# The number of assigned IP addresses has reached the upper limit.
LIMITEXCEEDED_ADDRESS = 'LimitExceeded.Address'

# The number of EIPs applied for exceeds the upper limit.
LIMITEXCEEDED_ADDRESSQUOTALIMITEXCEEDED = 'LimitExceeded.AddressQuotaLimitExceeded'

# Reached the upper limit of snapshot policies associated with an instance
LIMITEXCEEDED_ATTACHEDSNAPSHOTPOLICYEXCEEDED = 'LimitExceeded.AttachedSnapshotPolicyExceeded'

# Exceeded the upper limit of the bandwidth package quota.
LIMITEXCEEDED_BANDWIDTHPACKAGEQUOTA = 'LimitExceeded.BandwidthPackageQuota'

# 
LIMITEXCEEDED_BANDWIDTHPACKAGERESOURCEQUOTA = 'LimitExceeded.BandwidthPackageResourceQuota'

# Run out of the chances to change the IP.
LIMITEXCEEDED_CHANGEADDRESSQUOTA = 'LimitExceeded.ChangeAddressQuota'

# The number of assigned IP ranges of the VPC has reached the upper limit.
LIMITEXCEEDED_CIDRBLOCK = 'LimitExceeded.CidrBlock'

# Reached the upper limit of associated CCN instances
LIMITEXCEEDED_CURRENTINSTANCEATTACHEDCCNINSTANCES = 'LimitExceeded.CurrentInstanceAttachedCcnInstances'

# The number of EIPs applied for per day exceeds the upper limit.
LIMITEXCEEDED_DAILYALLOCATEADDRESSQUOTALIMITEXCEEDED = 'LimitExceeded.DailyAllocateAddressQuotaLimitExceeded'

# Run out of the daily chances to change the IP.
LIMITEXCEEDED_DAILYCHANGEADDRESSQUOTA = 'LimitExceeded.DailyChangeAddressQuota'

# Exceeded the upper limit of the EIPs bound to the instance.
LIMITEXCEEDED_INSTANCEADDRESSQUOTA = 'LimitExceeded.InstanceAddressQuota'

# Ran out of the quota of chances to change the IP billing mode.
LIMITEXCEEDED_MODIFYADDRESSINTERNETCHARGETYPEQUOTA = 'LimitExceeded.ModifyAddressInternetChargeTypeQuota'

# Ran out of the monthly quota of chances to retrieve IPs.
LIMITEXCEEDED_MONTHLYADDRESSRECOVERYQUOTA = 'LimitExceeded.MonthlyAddressRecoveryQuota'

# Reached the upper limit of NAT gateways.
LIMITEXCEEDED_NATGATEWAYLIMITEXCEEDED = 'LimitExceeded.NatGatewayLimitExceeded'

# The number of NAT gateways created by the VPC has reached the upper limit.
LIMITEXCEEDED_NATGATEWAYPERVPCLIMITEXCEEDED = 'LimitExceeded.NatGatewayPerVpcLimitExceeded'

# Exceeded the character limit of a filter name.
LIMITEXCEEDED_NUMBEROFFILTERS = 'LimitExceeded.NumberOfFilters'

# The number of EIPs bound to the NAT gateway has reached the upper limit.
LIMITEXCEEDED_PUBLICIPADDRESSPERNATGATEWAYLIMITEXCEEDED = 'LimitExceeded.PublicIpAddressPerNatGatewayLimitExceeded'

# The number of security group rules exceeds the upper limit.
LIMITEXCEEDED_SECURITYGROUPPOLICYSET = 'LimitExceeded.SecurityGroupPolicySet'

# The number of subnet IP ranges assigned in the subnet has reached the upper limit.
LIMITEXCEEDED_SUBNETCIDRBLOCK = 'LimitExceeded.SubnetCidrBlock'

# Reached the upper limit of tag keys.
LIMITEXCEEDED_TAGKEYEXCEEDED = 'LimitExceeded.TagKeyExceeded'

# Reached the upper limit of tags keys per resource.
LIMITEXCEEDED_TAGKEYPERRESOURCEEXCEEDED = 'LimitExceeded.TagKeyPerResourceExceeded'

# Insufficient tag quota.
LIMITEXCEEDED_TAGNOTENOUGHQUOTA = 'LimitExceeded.TagNotEnoughQuota'

# Exceeded the tag quota. Unable to create resources.
LIMITEXCEEDED_TAGQUOTA = 'LimitExceeded.TagQuota'

# Reached the upper limit of tag quota.
LIMITEXCEEDED_TAGQUOTAEXCEEDED = 'LimitExceeded.TagQuotaExceeded'

# Reached the number limit of tag keys.
LIMITEXCEEDED_TAGTAGSEXCEEDED = 'LimitExceeded.TagTagsExceeded'

# Missing parameter.
MISSINGPARAMETER = 'MissingParameter'

# The specified public IP is isolated.
OPERATIONDENIED_ADDRESSINARREARS = 'OperationDenied.AddressInArrears'

# Mutually exclusive tasks are executing.
OPERATIONDENIED_MUTEXTASKRUNNING = 'OperationDenied.MutexTaskRunning'

# The resource is occupied.
RESOURCEINUSE = 'ResourceInUse'

# The specified IP address is already in use.
RESOURCEINUSE_ADDRESS = 'ResourceInUse.Address'

# Insufficient resources.
RESOURCEINSUFFICIENT = 'ResourceInsufficient'

# The IP range resources are insufficient.
RESOURCEINSUFFICIENT_CIDRBLOCK = 'ResourceInsufficient.CidrBlock'

# The subnet does not have sufficient IPs.
RESOURCEINSUFFICIENT_SUBNET = 'ResourceInsufficient.Subnet'

# The resource does not exist.
RESOURCENOTFOUND = 'ResourceNotFound'

# The Svc doesn't exist.
RESOURCENOTFOUND_SVCNOTEXIST = 'ResourceNotFound.SvcNotExist'

# The resource is unavailable.
RESOURCEUNAVAILABLE = 'ResourceUnavailable'

# The current user is not in the allowlist of the specified endpoint service.
RESOURCEUNAVAILABLE_SERVICEWHITELISTNOTADDED = 'ResourceUnavailable.ServiceWhiteListNotAdded'

# Unauthorized operation.
UNAUTHORIZEDOPERATION = 'UnauthorizedOperation'

# No permission to apply for AnycastEip resources.
UNAUTHORIZEDOPERATION_ANYCASTEIP = 'UnauthorizedOperation.AnycastEip'

# The binding relationship does not exist.
UNAUTHORIZEDOPERATION_ATTACHMENTNOTFOUND = 'UnauthorizedOperation.AttachmentNotFound'

# Unauthorized user.
UNAUTHORIZEDOPERATION_INVALIDACCOUNT = 'UnauthorizedOperation.InvalidAccount'

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

# This account is not supported.
UNSUPPORTEDOPERATION_ACCOUNTNOTSUPPORTED = 'UnsupportedOperation.AccountNotSupported'

# The port does not exist.
UNSUPPORTEDOPERATION_ACTIONNOTFOUND = 'UnsupportedOperation.ActionNotFound'

# 
UNSUPPORTEDOPERATION_ADDRESSIPNOTSUPPORTINSTANCE = 'UnsupportedOperation.AddressIpNotSupportInstance'

# This operation is not supported by the IP address status.
UNSUPPORTEDOPERATION_ADDRESSSTATUSNOTPERMIT = 'UnsupportedOperation.AddressStatusNotPermit'

# The resource is not under the specified AppId.
UNSUPPORTEDOPERATION_APPIDMISMATCH = 'UnsupportedOperation.AppIdMismatch'

# The APPId doesn't exist.
UNSUPPORTEDOPERATION_APPIDNOTFOUND = 'UnsupportedOperation.AppIdNotFound'

# The NAT gateway route already exists in another VPC added to the CCN instance.
UNSUPPORTEDOPERATION_ASSOCIATEDVPCOFCCNHADNATROUTE = 'UnsupportedOperation.AssociatedVpcOfCcnHadNatRoute'

# The EIP is already bound to a CVM.
UNSUPPORTEDOPERATION_ATTACHMENTALREADYEXISTS = 'UnsupportedOperation.AttachmentAlreadyExists'

# The binding relationship does not exist.
UNSUPPORTEDOPERATION_ATTACHMENTNOTFOUND = 'UnsupportedOperation.AttachmentNotFound'

# Unable to delete the current CCN instance: its monthly-subscribed bandwidth does not expire. 
UNSUPPORTEDOPERATION_BANDWIDTHNOTEXPIRED = 'UnsupportedOperation.BandwidthNotExpired'

# This bandwidth package does not support this operation.
UNSUPPORTEDOPERATION_BANDWIDTHPACKAGEIDNOTSUPPORTED = 'UnsupportedOperation.BandwidthPackageIdNotSupported'

# EIP has already been bound.
UNSUPPORTEDOPERATION_BINDEIP = 'UnsupportedOperation.BindEIP'

# The specified VPC CIDR range does not support Classiclink.
UNSUPPORTEDOPERATION_CIDRUNSUPPORTEDCLASSICLINK = 'UnsupportedOperation.CIDRUnSupportedClassicLink'

# The instance is already associated with a CCN.
UNSUPPORTEDOPERATION_CCNATTACHED = 'UnsupportedOperation.CcnAttached'

# You cannot associated the CCN instance with resources under other Tencent Cloud accounts. 
UNSUPPORTEDOPERATION_CCNCROSSACCOUNT = 'UnsupportedOperation.CcnCrossAccount'

# This CCN instance cannot be deleted as it has flow logs.
UNSUPPORTEDOPERATION_CCNHASFLOWLOG = 'UnsupportedOperation.CcnHasFlowLog'

# The instance is not associated with a CCN.
UNSUPPORTEDOPERATION_CCNNOTATTACHED = 'UnsupportedOperation.CcnNotAttached'

# In cross-account association, instances under an Auto-Driving Cloud account cannot be associated with CCNs created under an ordinary account.
UNSUPPORTEDOPERATION_CCNORDINARYACCOUNTREFUSEATTACH = 'UnsupportedOperation.CcnOrdinaryAccountRefuseAttach'

# The specified route table does not exist.
UNSUPPORTEDOPERATION_CCNROUTETABLENOTEXIST = 'UnsupportedOperation.CcnRouteTableNotExist'

# CDC subnet can only create a route to the local gateway.
UNSUPPORTEDOPERATION_CDCSUBNETNOTSUPPORTUNLOCALGATEWAY = 'UnsupportedOperation.CdcSubnetNotSupportUnLocalGateway'

# The instance has already been bound to the VPC.
UNSUPPORTEDOPERATION_CLASSICINSTANCEIDALREADYEXISTS = 'UnsupportedOperation.ClassicInstanceIdAlreadyExists'

# Reached the upper limit of security group policies of the load balancer.
UNSUPPORTEDOPERATION_CLBPOLICYEXCEEDLIMIT = 'UnsupportedOperation.ClbPolicyExceedLimit'

# Public network CLB does not support this policy.
UNSUPPORTEDOPERATION_CLBPOLICYLIMIT = 'UnsupportedOperation.ClbPolicyLimit'

# The IP range overlaps with that of the TKE container under the VPC.
UNSUPPORTEDOPERATION_CONFLICTWITHDOCKERROUTE = 'UnsupportedOperation.ConflictWithDockerRoute'

# Unable to delete: There’re NAT rules associated with this direct connect gateway. Please delete all NAT rules first. 
UNSUPPORTEDOPERATION_DCGATEWAYNATRULEEXISTS = 'UnsupportedOperation.DCGatewayNatRuleExists'

# No direct connect gateway exists in the specified VPC.
UNSUPPORTEDOPERATION_DCGATEWAYSNOTFOUNDINVPC = 'UnsupportedOperation.DcGatewaysNotFoundInVpc'

# Unable to delete: This is the default route table.
UNSUPPORTEDOPERATION_DELDEFAULTROUTE = 'UnsupportedOperation.DelDefaultRoute'

# Unable to delete: This is a route table associated with a subnet.
UNSUPPORTEDOPERATION_DELROUTEWITHSUBNET = 'UnsupportedOperation.DelRouteWithSubnet'

# 
UNSUPPORTEDOPERATION_DELETEVPNCONNINVALIDSTATE = 'UnsupportedOperation.DeleteVpnConnInvalidState'

# Direct connect gateway is updating the BGP Community attribute.
UNSUPPORTEDOPERATION_DIRECTCONNECTGATEWAYISUPDATINGCOMMUNITY = 'UnsupportedOperation.DirectConnectGatewayIsUpdatingCommunity'

# The specified routing policy cannot be re-published to CCN. Please first withdraw it from CCN.
UNSUPPORTEDOPERATION_DISABLEDNOTIFYCCN = 'UnsupportedOperation.DisabledNotifyCcn'

# To create a DPDK NAT flow log, the collection type must be `All`.
UNSUPPORTEDOPERATION_DPDKNATFLOWLOGONLYSUPPORTALLTRAFFICTYPE = 'UnsupportedOperation.DpdkNatFlowLogOnlySupportAllTrafficType'

# The security group policies are repeated.
UNSUPPORTEDOPERATION_DUPLICATEPOLICY = 'UnsupportedOperation.DuplicatePolicy'

# ECMP is not supported.
UNSUPPORTEDOPERATION_ECMP = 'UnsupportedOperation.Ecmp'

# Form an ECMP with the CCN route.
UNSUPPORTEDOPERATION_ECMPWITHCCNROUTE = 'UnsupportedOperation.EcmpWithCcnRoute'

# Form an ECMP with the user’s custom routes.
UNSUPPORTEDOPERATION_ECMPWITHUSERROUTE = 'UnsupportedOperation.EcmpWithUserRoute'

# Multi-cast is not available in the current region.
UNSUPPORTEDOPERATION_ENABLEMULTICAST = 'UnsupportedOperation.EnableMulticast'

# The endpoint service itself cannot be set as the endpoint.
UNSUPPORTEDOPERATION_ENDPOINTSERVICE = 'UnsupportedOperation.EndPointService'

# 
UNSUPPORTEDOPERATION_FLOWLOGINSTANCEEXISTED = 'UnsupportedOperation.FlowLogInstanceExisted'

# Unable to create a flow log: the current ENI is bound with a KO model.
UNSUPPORTEDOPERATION_FLOWLOGSNOTSUPPORTKOINSTANCEENI = 'UnsupportedOperation.FlowLogsNotSupportKoInstanceEni'

# Unable to create a flow log: the current ENI is not bound to an instance.
UNSUPPORTEDOPERATION_FLOWLOGSNOTSUPPORTNULLINSTANCEENI = 'UnsupportedOperation.FlowLogsNotSupportNullInstanceEni'

# This type of address does not support this operation.
UNSUPPORTEDOPERATION_INCORRECTADDRESSRESOURCETYPE = 'UnsupportedOperation.IncorrectAddressResourceType'

# The configured instance does not match with the route table.
UNSUPPORTEDOPERATION_INSTANCEANDRTBNOTMATCH = 'UnsupportedOperation.InstanceAndRtbNotMatch'

# The specified instance resource does not match.
UNSUPPORTEDOPERATION_INSTANCEMISMATCH = 'UnsupportedOperation.InstanceMismatch'

# In cross-account association, instances under an ordinary account cannot be associated with CCNs created under an Auto-Driving Cloud account.
UNSUPPORTEDOPERATION_INSTANCEORDINARYACCOUNTREFUSEATTACH = 'UnsupportedOperation.InstanceOrdinaryAccountRefuseAttach'

# This operation is not supported by the status of the instance bound with the IP address.
UNSUPPORTEDOPERATION_INSTANCESTATENOTSUPPORTED = 'UnsupportedOperation.InstanceStateNotSupported'

# Insufficient account balance.
UNSUPPORTEDOPERATION_INSUFFICIENTFUNDS = 'UnsupportedOperation.InsufficientFunds'

# Unsupported operation.
UNSUPPORTEDOPERATION_INVALIDACTION = 'UnsupportedOperation.InvalidAction'

# This operation is not allowed under the network billing mode of the IP address.
UNSUPPORTEDOPERATION_INVALIDADDRESSINTERNETCHARGETYPE = 'UnsupportedOperation.InvalidAddressInternetChargeType'

# This operation is not supported by the IP address status.
UNSUPPORTEDOPERATION_INVALIDADDRESSSTATE = 'UnsupportedOperation.InvalidAddressState'

# Invalid instance status.
UNSUPPORTEDOPERATION_INVALIDINSTANCESTATE = 'UnsupportedOperation.InvalidInstanceState'

# This operation is not allowed under this billing mode.
UNSUPPORTEDOPERATION_INVALIDRESOURCEINTERNETCHARGETYPE = 'UnsupportedOperation.InvalidResourceInternetChargeType'

# Bandwidth packages inapplicable to this protocol
UNSUPPORTEDOPERATION_INVALIDRESOURCEPROTOCOL = 'UnsupportedOperation.InvalidResourceProtocol'

# Invalid resource status.
UNSUPPORTEDOPERATION_INVALIDSTATE = 'UnsupportedOperation.InvalidState'

# The current status of the route does not support publishing to CCN. Please retry later.
UNSUPPORTEDOPERATION_INVALIDSTATUSNOTIFYCCN = 'UnsupportedOperation.InvalidStatusNotifyCcn'

# The account of the instance associated with the current CCN is not a Financial Cloud account.
UNSUPPORTEDOPERATION_ISNOTFINANCEACCOUNT = 'UnsupportedOperation.IsNotFinanceAccount'

# This ISP does not support this operation.
UNSUPPORTEDOPERATION_ISPNOTSUPPORTED = 'UnsupportedOperation.IspNotSupported'

# The specified CDC instance already has a local gateway.
UNSUPPORTEDOPERATION_LOCALGATEWAYALREADYEXISTS = 'UnsupportedOperation.LocalGatewayAlreadyExists'

# 
UNSUPPORTEDOPERATION_LOCKEDRESOURCES = 'UnsupportedOperation.LockedResources'

# The account does not support modifying this attribute of the public IP.
UNSUPPORTEDOPERATION_MODIFYADDRESSATTRIBUTE = 'UnsupportedOperation.ModifyAddressAttribute'

# The resource mutual exclusion operation is being executed.
UNSUPPORTEDOPERATION_MUTEXOPERATIONTASKRUNNING = 'UnsupportedOperation.MutexOperationTaskRunning'

# The public IP of the NAT gateway does not exist. 
UNSUPPORTEDOPERATION_NATGATEWAYEIPNOTEXISTS = 'UnsupportedOperation.NatGatewayEipNotExists'

# There are IPs associated with this NAT gateway.
UNSUPPORTEDOPERATION_NATGATEWAYHADEIPUNASSOCIATE = 'UnsupportedOperation.NatGatewayHadEipUnassociate'

# The private IP specified in the SNAT/DNAT forwarding rule has been bound with another rule.
UNSUPPORTEDOPERATION_NATGATEWAYRULEPIPEXISTS = 'UnsupportedOperation.NatGatewayRulePipExists'

# The private IP of the SNAT translation rule must be within the IP range of the VM ENI.
UNSUPPORTEDOPERATION_NATGATEWAYSNATPIPNEEDVM = 'UnsupportedOperation.NatGatewaySnatPipNeedVm'

# The SNAT forwarding rule of the NAT gateway does not exist.
UNSUPPORTEDOPERATION_NATGATEWAYSNATRULENOTEXISTS = 'UnsupportedOperation.NatGatewaySnatRuleNotExists'

# The specified NAT Gateway type does not support configuring a SNAT rule.
UNSUPPORTEDOPERATION_NATGATEWAYTYPENOTSUPPORTSNAT = 'UnsupportedOperation.NatGatewayTypeNotSupportSNAT'

# The NAT instance does not support this operation.
UNSUPPORTEDOPERATION_NATNOTSUPPORTED = 'UnsupportedOperation.NatNotSupported'

# The specified subnet does not support creating a route to the local gateway.
UNSUPPORTEDOPERATION_NORMALSUBNETNOTSUPPORTLOCALGATEWAY = 'UnsupportedOperation.NormalSubnetNotSupportLocalGateway'

# This operation is not allowed because the current instance is blocked.
UNSUPPORTEDOPERATION_NOTLOCKEDINSTANCEOPERATION = 'UnsupportedOperation.NotLockedInstanceOperation'

# The target service specified does not match the one specified in the IP application.
UNSUPPORTEDOPERATION_NOTMATCHTARGETSERVICE = 'UnsupportedOperation.NotMatchTargetService'

# Unsupported operation: the current CCN instance is not in “Applying” status.
UNSUPPORTEDOPERATION_NOTPENDINGCCNINSTANCE = 'UnsupportedOperation.NotPendingCcnInstance'

# Unsupported operation: the current CCN instance is not billed on a pay-as-you-go basis.
UNSUPPORTEDOPERATION_NOTPOSTPAIDCCNOPERATION = 'UnsupportedOperation.NotPostpaidCcnOperation'

# A CCN instance cannot be associated with an edge instance and a cross-boarder instance at the same time. 
UNSUPPORTEDOPERATION_NOTSUPPORTATTACHEDGEANDCROSSBORDERINSTANCE = 'UnsupportedOperation.NotSupportAttachEdgeAndCrossBorderInstance'

# The default route table cannot be deleted.
UNSUPPORTEDOPERATION_NOTSUPPORTDELETEDEFAULTROUTETABLE = 'UnsupportedOperation.NotSupportDeleteDefaultRouteTable'

# This type of addresses cannot be released.
UNSUPPORTEDOPERATION_NOTSUPPORTEDADDRESSIPSCHARGETYPE = 'UnsupportedOperation.NotSupportedAddressIpsChargeType'

# 
UNSUPPORTEDOPERATION_NOTSUPPORTEDPURCHASECENTEREGRESSRESOURCE = 'UnsupportedOperation.NotSupportedPurchaseCenterEgressResource'

# The current CCN instance does not support publishing update routes.
UNSUPPORTEDOPERATION_NOTSUPPORTEDUPDATECCNROUTEPUBLISH = 'UnsupportedOperation.NotSupportedUpdateCcnRoutePublish'

# The specified routing policy cannot be published to or withdrawn from CCN.
UNSUPPORTEDOPERATION_NOTIFYCCN = 'UnsupportedOperation.NotifyCcn'

# This billing mode is disused. Please try another billing mode.
UNSUPPORTEDOPERATION_OFFLINECHARGETYPE = 'UnsupportedOperation.OfflineChargeType'

# Only the Ckafka Pro Edition is supported.
UNSUPPORTEDOPERATION_ONLYSUPPORTPROFESSIONKAFKA = 'UnsupportedOperation.OnlySupportProfessionKafka'

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

# The current account can not use this service in the current region.
UNSUPPORTEDOPERATION_PURCHASELIMIT = 'UnsupportedOperation.PurchaseLimit'

# This record already exists.
UNSUPPORTEDOPERATION_RECORDEXISTS = 'UnsupportedOperation.RecordExists'

# The record does not exist.
UNSUPPORTEDOPERATION_RECORDNOTEXISTS = 'UnsupportedOperation.RecordNotExists'

# Operation prohibited: The resource is not available.
UNSUPPORTEDOPERATION_RESOURCEISINVALIDSTATE = 'UnsupportedOperation.ResourceIsInvalidState'

# The resource ID entered does not match with any resource bound with the IP. Check and try again.
UNSUPPORTEDOPERATION_RESOURCEMISMATCH = 'UnsupportedOperation.ResourceMismatch'

# No roles available. Please confirm whether you get the authorization for the role.
UNSUPPORTEDOPERATION_ROLENOTFOUND = 'UnsupportedOperation.RoleNotFound'

# The routing table is bound to a subnet.
UNSUPPORTEDOPERATION_ROUTETABLEHASSUBNETRULE = 'UnsupportedOperation.RouteTableHasSubnetRule'

# This instance is already associated with a snapshot policy. 
UNSUPPORTEDOPERATION_SNAPSHOTATTACHED = 'UnsupportedOperation.SnapshotAttached'

# Snapshot backup policy cannot be modified. 
UNSUPPORTEDOPERATION_SNAPSHOTBACKUPTYPEMODIFY = 'UnsupportedOperation.SnapshotBackupTypeModify'

# Failed to generate the snapshot file.
UNSUPPORTEDOPERATION_SNAPSHOTFILEFAILED = 'UnsupportedOperation.SnapshotFileFailed'

# The snapshot file is expired or has been deleted.
UNSUPPORTEDOPERATION_SNAPSHOTFILENOEXIST = 'UnsupportedOperation.SnapshotFileNoExist'

# Generating the snapshot file…Please check again later.
UNSUPPORTEDOPERATION_SNAPSHOTFILEPROCESSING = 'UnsupportedOperation.SnapshotFileProcessing'

# Batch association only supports instances in the same region.
UNSUPPORTEDOPERATION_SNAPSHOTINSTANCEREGIONDIFF = 'UnsupportedOperation.SnapshotInstanceRegionDiff'

# The instance is not associated with any snapshot policy.
UNSUPPORTEDOPERATION_SNAPSHOTNOTATTACHED = 'UnsupportedOperation.SnapshotNotAttached'

# The SNAT subnet does not support assigning IPs.
UNSUPPORTEDOPERATION_SNATSUBNET = 'UnsupportedOperation.SnatSubnet'

# The endpoint created by the specified endpoint service cannot be bound to a security group.
UNSUPPORTEDOPERATION_SPECIALENDPOINTSERVICE = 'UnsupportedOperation.SpecialEndPointService'

# The relayed ENI does not support this operation.
UNSUPPORTEDOPERATION_SUBENINOTSUPPORTTRUNKING = 'UnsupportedOperation.SubEniNotSupportTrunking'

# 
UNSUPPORTEDOPERATION_SUBNETNOTEXISTS = 'UnsupportedOperation.SubnetNotExists'

# System route. Operation is prohibited.
UNSUPPORTEDOPERATION_SYSTEMROUTE = 'UnsupportedOperation.SystemRoute'

# Tags are being assigned.
UNSUPPORTEDOPERATION_TAGALLOCATE = 'UnsupportedOperation.TagAllocate'

# Tags are being released.
UNSUPPORTEDOPERATION_TAGFREE = 'UnsupportedOperation.TagFree'

# Unauthorized for this tag.
UNSUPPORTEDOPERATION_TAGNOTPERMIT = 'UnsupportedOperation.TagNotPermit'

# The specified tag key is reserved for system usage.
UNSUPPORTEDOPERATION_TAGSYSTEMRESERVEDTAGKEY = 'UnsupportedOperation.TagSystemReservedTagKey'

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

# Overdue payments are found under this account. Please complete the payment first.
UNSUPPORTEDOPERATION_UNPAIDORDERALREADYEXISTS = 'UnsupportedOperation.UnpaidOrderAlreadyExists'

# Binding the EIPs specified in `LocalZone` is not supported.
UNSUPPORTEDOPERATION_UNSUPPORTEDBINDLOCALZONEEIP = 'UnsupportedOperation.UnsupportedBindLocalZoneEIP'

# The specified instance type does not support ENIs.
UNSUPPORTEDOPERATION_UNSUPPORTEDINSTANCEFAMILY = 'UnsupportedOperation.UnsupportedInstanceFamily'

# The service is not available in this country/region.
UNSUPPORTEDOPERATION_UNSUPPORTEDREGION = 'UnsupportedOperation.UnsupportedRegion'

# The selected CCN instance cannot be created because the payment type is not supported.
UNSUPPORTEDOPERATION_USERANDCCNCHARGETYPENOTMATCH = 'UnsupportedOperation.UserAndCcnChargeTypeNotMatch'

# The specified version number of the security group policy is inconsistent with the latest version.
UNSUPPORTEDOPERATION_VERSIONMISMATCH = 'UnsupportedOperation.VersionMismatch'

# The resources are not in the same VPC.
UNSUPPORTEDOPERATION_VPCMISMATCH = 'UnsupportedOperation.VpcMismatch'

# Operation failed: The tunnel is not available now.
UNSUPPORTEDOPERATION_VPNCONNINVALIDSTATE = 'UnsupportedOperation.VpnConnInvalidState'

# 
UNSUPPORTEDOPERATION_VPNGWVPCIDMUSTHAVE = 'UnsupportedOperation.VpnGwVpcIdMustHave'

# The specified resources are not in the same availability zone.
UNSUPPORTEDOPERATION_ZONEMISMATCH = 'UnsupportedOperation.ZoneMismatch'

# The maximum number of VPC resource requests for the specified region has been reached.
VPCLIMITEXCEEDED = 'VpcLimitExceeded'
