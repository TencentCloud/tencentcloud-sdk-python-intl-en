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


# Authentication failed.
AUTHFAILURE_UNAUTHORIZEDOPERATION = 'AuthFailure.UnauthorizedOperation'

# Operation failed.
FAILEDOPERATION = 'FailedOperation'

# Insufficient balance.
FAILEDOPERATION_BLOCKBALANCE = 'FailedOperation.BlockBalance'

# Data operation failed.
FAILEDOPERATION_DATAOPERATIONFAILED = 'FailedOperation.DataOperationFailed'

# The image is in use.
FAILEDOPERATION_IMAGEINUSE = 'FailedOperation.ImageInUse'

# An instance already exists under the module.
FAILEDOPERATION_INSTANCEINMODULE = 'FailedOperation.InstanceInModule'

# Not all instances are shut down.
FAILEDOPERATION_INSTANCENOTALLSTOPPED = 'FailedOperation.InstanceNotAllStopped'

# The instance does not belong to the current module.
FAILEDOPERATION_INSTANCEOWNERCHECKFAILED = 'FailedOperation.InstanceOwnerCheckFailed'

# Internal error.
FAILEDOPERATION_INTERNALOPERATIONFAILURE = 'FailedOperation.InternalOperationFailure'

# This operation cannot be performed in the current status.
FAILEDOPERATION_INVALIDSTATUS = 'FailedOperation.InvalidStatus'

# The current operation cannot be performed as another operation is being performed.
FAILEDOPERATION_OPERATIONCONFLICT = 'FailedOperation.OperationConflict'

# The current operation is not allowed.
FAILEDOPERATION_OPERATIONNOTALLOW = 'FailedOperation.OperationNotAllow'

# The private IP has been bound to an EIP.
FAILEDOPERATION_PRIVATEIPADDRESSBINDED = 'FailedOperation.PrivateIpAddressBinded'

# The private IP is unavailable.
FAILEDOPERATION_PRIVATEIPADDRESSUNAVAILABLE = 'FailedOperation.PrivateIpAddressUnavailable'

# Internal error.
INTERNALERROR = 'InternalError'

# The parameter is incorrect.
INVALIDPARAMETER = 'InvalidParameter'

# The parameters cannot be specified at the same time.
INVALIDPARAMETER_COEXIST = 'InvalidParameter.Coexist'

# The parameter format is incorrect.
INVALIDPARAMETER_FORMATERROR = 'InvalidParameter.FormatError'

# The data format is incorrect.
INVALIDPARAMETER_INVALIDDATAFORMAT = 'InvalidParameter.InvalidDataFormat'

# The two specified parameters conflict. An EIP can only be bound to an instance or the specified private IP of the specified ENI.
INVALIDPARAMETER_INVALIDPARAMETERCONFLICT = 'InvalidParameter.InvalidParameterConflict'

# The CLB instance ID is incorrect.
INVALIDPARAMETER_LBIDNOTFOUND = 'InvalidParameter.LBIdNotFound'

# The listener ID is incorrect.
INVALIDPARAMETER_LISTENERIDNOTFOUND = 'InvalidParameter.ListenerIdNotFound'

# No eligible forwarding rules were found.
INVALIDPARAMETER_LOCATIONNOTFOUND = 'InvalidParameter.LocationNotFound'

# Only `KeepImageLogin`, `Password`, or `KeyIds` can be used at a time.
INVALIDPARAMETER_PARAMETERCONFLICT = 'InvalidParameter.ParameterConflict'

# Listener port check failed due to a port conflict.
INVALIDPARAMETER_PORTCHECKFAILED = 'InvalidParameter.PortCheckFailed'

# Listener protocol check failed, because this operation is not supported by the protocol.
INVALIDPARAMETER_PROTOCOLCHECKFAILED = 'InvalidParameter.ProtocolCheckFailed'

# The region is invalid.
INVALIDPARAMETER_REGIONNOTFOUND = 'InvalidParameter.RegionNotFound'

# The parameter value is incorrect.
INVALIDPARAMETERVALUE = 'InvalidParameterValue'

# The number applied for exceeds the limit.
INVALIDPARAMETERVALUE_ADDRESSQUOTALIMITEXCEEDED = 'InvalidParameterValue.AddressQuotaLimitExceeded'

# The bandwidth exceeds the limit.
INVALIDPARAMETERVALUE_BANDWIDTHOUTOFRANGE = 'InvalidParameterValue.BandwidthOutOfRange'

# The destination IP range is not within the CIDR range of the customer VPC.
INVALIDPARAMETERVALUE_CIDRNOTINPEERVPC = 'InvalidParameterValue.CidrNotInPeerVpc'

# The data is duplicate.
INVALIDPARAMETERVALUE_DUPLICATE = 'InvalidParameterValue.Duplicate'

# The value of the `Filter` parameter exceeds the limit.
INVALIDPARAMETERVALUE_FILTERLIMITEXCEEDED = 'InvalidParameterValue.FilterLimitExceeded'

# An image has already been imported.
INVALIDPARAMETERVALUE_IMAGEDUPLICATE = 'InvalidParameterValue.ImageDuplicate'

# The image name is duplicate.
INVALIDPARAMETERVALUE_IMAGENAMEDUPLICATE = 'InvalidParameterValue.ImageNameDuplicate'

# The image size is greater than the system disk size.
INVALIDPARAMETERVALUE_IMAGESIZELARGETHANSYSDISKSIZE = 'InvalidParameterValue.ImageSizeLargeThanSysDiskSize'

# The instance configuration does not match.
INVALIDPARAMETERVALUE_INSTANCECONFIGNOTMATCH = 'InvalidParameterValue.InstanceConfigNotMatch'

# The instance does not support the current operation.
INVALIDPARAMETERVALUE_INSTANCEIDNOTSUPPORTED = 'InvalidParameterValue.InstanceIdNotSupported'

# The instance name length exceeds the limit.
INVALIDPARAMETERVALUE_INSTANCENAMETOOLONG = 'InvalidParameterValue.InstanceNameTooLong'

# The instance model and `pid` do not match.
INVALIDPARAMETERVALUE_INSTANCETYPENOTMATCHPID = 'InvalidParameterValue.InstanceTypeNotMatchPid'

# The EIP is invalid.
INVALIDPARAMETERVALUE_INVAILDADDRESSID = 'InvalidParameterValue.InvaildAddressId'

# Your input is incorrect, or you have no permission for the operation.
INVALIDPARAMETERVALUE_INVAILDDESCRIBEINSTANCE = 'InvalidParameterValue.InvaildDescribeInstance'

# The ENI ID is invalid.
INVALIDPARAMETERVALUE_INVAILDENIID = 'InvalidParameterValue.InvaildEniID'

# `HostName` is invalid.
INVALIDPARAMETERVALUE_INVAILDHOSTNAME = 'InvalidParameterValue.InvaildHostName'

# The parameter is incorrect.
INVALIDPARAMETERVALUE_INVAILDMODIFYPARAM = 'InvalidParameterValue.InvaildModifyParam'

# The number of modules is invalid.
INVALIDPARAMETERVALUE_INVAILDMODULENUM = 'InvalidParameterValue.InvaildModuleNum'

# The pagination parameter is invalid.
INVALIDPARAMETERVALUE_INVAILDPAGEPARAM = 'InvalidParameterValue.InvaildPageParam'

# The password is invalid.
INVALIDPARAMETERVALUE_INVAILDPASSWORD = 'InvalidParameterValue.InvaildPassword'

# When you bind an ENI synchronously, you can apply for only one EIP at a time.
INVALIDPARAMETERVALUE_INVALIDADDRESSCOUNT = 'InvalidParameterValue.InvalidAddressCount'

# The bandwidth size is invalid.
INVALIDPARAMETERVALUE_INVALIDBANDWIDTH = 'InvalidParameterValue.InvalidBandwidth'

# The inbound bandwidth size exceeds the limit.
INVALIDPARAMETERVALUE_INVALIDBANDWIDTHIN = 'InvalidParameterValue.InvalidBandwidthIn'

# The inbound and outbound bandwidth must be the same.
INVALIDPARAMETERVALUE_INVALIDBANDWIDTHINANDOUT = 'InvalidParameterValue.InvalidBandwidthInAndOut'

# The selected billing mode is not supported.
INVALIDPARAMETERVALUE_INVALIDBILLINGTYPE = 'InvalidParameterValue.InvalidBillingType'

# The number of data disks is invalid.
INVALIDPARAMETERVALUE_INVALIDDATADISKNUM = 'InvalidParameterValue.InvalidDataDiskNum'

# The data disk size is invalid.
INVALIDPARAMETERVALUE_INVALIDDATADISKSIZE = 'InvalidParameterValue.InvalidDataDiskSize'

# The data disk type is invalid.
INVALIDPARAMETERVALUE_INVALIDDATADISKTYPE = 'InvalidParameterValue.InvalidDataDiskType'

# Windows images do not support IP direct access.
INVALIDPARAMETERVALUE_INVALIDEIPDIRECTSERVICE = 'InvalidParameterValue.InvalidEIPDirectService'

# The region parameter is invalid.
INVALIDPARAMETERVALUE_INVALIDECMREGION = 'InvalidParameterValue.InvalidEcmRegion'

# The filter is invalid.
INVALIDPARAMETERVALUE_INVALIDFILTER = 'InvalidParameterValue.InvalidFilter'

# The ISP is invalid.
INVALIDPARAMETERVALUE_INVALIDISPINNODE = 'InvalidParameterValue.InvalidISPInNode'

# Models with a memory of 4 GB or above do not support 32-bit OS images.
INVALIDPARAMETERVALUE_INVALIDIMAGEARCHITECTURE = 'InvalidParameterValue.InvalidImageArchitecture'

# The image ID is invalid.
INVALIDPARAMETERVALUE_INVALIDIMAGEID = 'InvalidParameterValue.InvalidImageID'

# The billing mode of the instance is invalid.
INVALIDPARAMETERVALUE_INVALIDINSTANCECHARGETYPE = 'InvalidParameterValue.InvalidInstanceChargeType'

# The instance ID is invalid.
INVALIDPARAMETERVALUE_INVALIDINSTANCEID = 'InvalidParameterValue.InvalidInstanceID'

# The configuration of a High-IO model cannot be adjusted.
INVALIDPARAMETERVALUE_INVALIDINSTANCETYPE = 'InvalidParameterValue.InvalidInstanceType'

# The model ID is invalid.
INVALIDPARAMETERVALUE_INVALIDINSTANCETYPECONFIGID = 'InvalidParameterValue.InvalidInstanceTypeConfigID'

# The billing mode is invalid.
INVALIDPARAMETERVALUE_INVALIDINTERNETCHARGETYPE = 'InvalidParameterValue.InvalidInternetChargeType'

# Invalid key ID.
INVALIDPARAMETERVALUE_INVALIDKEYPAIRID = 'InvalidParameterValue.InvalidKeyPairId'

# Invalid key name.
INVALIDPARAMETERVALUE_INVALIDKEYPAIRNAME = 'InvalidParameterValue.InvalidKeyPairName'

# The number of CLB instances is invalid.
INVALIDPARAMETERVALUE_INVALIDLOADBALANCERNUM = 'InvalidParameterValue.InvalidLoadBalancerNum'

# The CLB instance type is invalid.
INVALIDPARAMETERVALUE_INVALIDLOADBALANCERTYPE = 'InvalidParameterValue.InvalidLoadBalancerType'

# The module ID is invalid.
INVALIDPARAMETERVALUE_INVALIDMODULEID = 'InvalidParameterValue.InvalidModuleID'

# The `ModuleId` and `InstanceType` parameters cannot be both empty.
INVALIDPARAMETERVALUE_INVALIDMODULEIDANDINSTANCETYPECONFIGID = 'InvalidParameterValue.InvalidModuleIDAndInstanceTypeConfigID'

# The `ModuleId` and `InstanceType` parameters cannot be both empty.
INVALIDPARAMETERVALUE_INVALIDMODULEIDANDINSTANCETYPEID = 'InvalidParameterValue.InvalidModuleIDAndInstanceTypeID'

# The module names conflict.
INVALIDPARAMETERVALUE_INVALIDMODULENAME = 'InvalidParameterValue.InvalidModuleName'

# The sort field is invalid.
INVALIDPARAMETERVALUE_INVALIDORDERBYFIELD = 'InvalidParameterValue.InvalidOrderByField'

# The common parameter is invalid.
INVALIDPARAMETERVALUE_INVALIDPUBLICPARAM = 'InvalidParameterValue.InvalidPublicParam'

# The ECM region is invalid.
INVALIDPARAMETERVALUE_INVALIDREGION = 'InvalidParameterValue.InvalidRegion'

# The security group ID is invalid.
INVALIDPARAMETERVALUE_INVALIDSECURITYGROUPID = 'InvalidParameterValue.InvalidSecurityGroupID'

# InvalidParameterValue.InvalidSnapshot
INVALIDPARAMETERVALUE_INVALIDSNAPSHOT = 'InvalidParameterValue.InvalidSnapshot'

# InvalidParameterValue.InvalidSnapshotId
INVALIDPARAMETERVALUE_INVALIDSNAPSHOTID = 'InvalidParameterValue.InvalidSnapshotId'

# The node does not exist in this subnet.
INVALIDPARAMETERVALUE_INVALIDSUBNETINZONE = 'InvalidParameterValue.InvalidSubnetInZone'

# The system disk size is invalid.
INVALIDPARAMETERVALUE_INVALIDSYSTEMDISKSIZE = 'InvalidParameterValue.InvalidSystemDiskSize'

# The system disk type is invalid.
INVALIDPARAMETERVALUE_INVALIDSYSTEMDISKTYPE = 'InvalidParameterValue.InvalidSystemDiskType'

# The time is invalid.
INVALIDPARAMETERVALUE_INVALIDTIME = 'InvalidParameterValue.InvalidTime'

# The zone is invalid.
INVALIDPARAMETERVALUE_INVALIDZONE = 'InvalidParameterValue.InvalidZone'

# The city or quantity is invalid.
INVALIDPARAMETERVALUE_INVALIDZONEINSTANCECOUNT = 'InvalidParameterValue.InvalidZoneInstanceCount'

# This model is not supported in the AZ.
INVALIDPARAMETERVALUE_INVALIDZONEINSTANCETYPE = 'InvalidParameterValue.InvalidZoneInstanceType'

# The parameter length is incorrect.
INVALIDPARAMETERVALUE_LENGTH = 'InvalidParameterValue.Length'

# The parameter value exceeds the limit.
INVALIDPARAMETERVALUE_LIMITEXCEEDED = 'InvalidParameterValue.LimitExceeded'

# The input parameter format is invalid.
INVALIDPARAMETERVALUE_MALFORMED = 'InvalidParameterValue.Malformed'

# The default configuration of an ECM module associated with instances cannot be modified.
INVALIDPARAMETERVALUE_MODULENOTALLOWCHANGE = 'InvalidParameterValue.ModuleNotAllowChange'

# The node does not support IPv6.
INVALIDPARAMETERVALUE_NODENOTSUPPORTIPV6 = 'InvalidParameterValue.NodeNotSupportIPv6'

# The object is not in the current subnet.
INVALIDPARAMETERVALUE_OBJECTNOTCURRENTSUBNET = 'InvalidParameterValue.ObjectNotCurrentSubnet'

# The specified object is not the current VPC.
INVALIDPARAMETERVALUE_OBJECTVPCNOTCURRENTVPC = 'InvalidParameterValue.ObjectVpcNotCurrentVpc'

# The parameter value exceeds the limit.
INVALIDPARAMETERVALUE_PARAMETERVALUETOOLARGE = 'InvalidParameterValue.ParameterValueTooLarge'

# The parameter value is not in the specified range.
INVALIDPARAMETERVALUE_RANGE = 'InvalidParameterValue.Range'

# The parameter value is an object retained by the system.
INVALIDPARAMETERVALUE_RESERVED = 'InvalidParameterValue.Reserved'

# The specified CIDR block conflicts with another subnet in the same VPC.
INVALIDPARAMETERVALUE_SUBNETCONFLICT = 'InvalidParameterValue.SubnetConflict'

# 
INVALIDPARAMETERVALUE_SUBNETNOTEXIST = 'InvalidParameterValue.SubnetNotExist'

# The subnet IP range is invalid.
INVALIDPARAMETERVALUE_SUBNETRANGE = 'InvalidParameterValue.SubnetRange'

# The number of tags exceeds the limit.
INVALIDPARAMETERVALUE_TAGNUMOUTOFRANGE = 'InvalidParameterValue.TagNumOutOfRange'

# The task was not found.
INVALIDPARAMETERVALUE_TASKNOTFOUND = 'InvalidParameterValue.TaskNotFound'

# The scheduled termination time is before the current time.
INVALIDPARAMETERVALUE_TERMINATETIMESMALLER = 'InvalidParameterValue.TerminateTimeSmaller'

# The parameter value is too long.
INVALIDPARAMETERVALUE_TOOLONG = 'InvalidParameterValue.TooLong'

# The model does not support the selected billing mode.
INVALIDPARAMETERVALUE_UNMATCHEDBILLINGTYPE = 'InvalidParameterValue.UnmatchedBillingType'

# The region is not supported.
INVALIDPARAMETERVALUE_UNSUPPORTEDREGION = 'InvalidParameterValue.UnsupportedRegion'

# IPv6 is not supported.
INVALIDPARAMETERVALUE_USERNOTSUPPORTIPV6 = 'InvalidParameterValue.UserNotSupportIPv6'

# The destination IP range conflicts with the CIDR block of the current VPC.
INVALIDPARAMETERVALUE_VPCCIDRCONFLICT = 'InvalidParameterValue.VpcCidrConflict'

# The quota limit is exceeded.
LIMITEXCEEDED = 'LimitExceeded'

# The number applied for exceeds the limit.
LIMITEXCEEDED_ADDRESSQUOTALIMITEXCEEDED = 'LimitExceeded.AddressQuotaLimitExceeded'

# The maximum number of applications has been reached. The maximum number of applications that can be made by a Tencent Cloud account per day in each region is equal to twice the quota.
LIMITEXCEEDED_ADDRESSQUOTALIMITEXCEEDEDDAILYALLOCATE = 'LimitExceeded.AddressQuotaLimitExceededDailyAllocate'

# Exceeded the upper limit of the assigned IPv6 IP ranges.
LIMITEXCEEDED_CIDRBLOCK = 'LimitExceeded.CidrBlock'

# The number of purchasable ENIs is insufficient.
LIMITEXCEEDED_ENIQUOTALIMITEXCEEDED = 'LimitExceeded.EniQuotaLimitExceeded'

# The number of security groups bound to the instance exceeds the limit.
LIMITEXCEEDED_INSTANCESECURITYGROUPLIMITEXCEEDED = 'LimitExceeded.InstanceSecurityGroupLimitExceeded'

# The number of CLB instances applied for exceeds the limit.
LIMITEXCEEDED_LBLIMITEXCEEDED = 'LimitExceeded.LBLimitExceeded'

# The number of default module security groups exceeds the limit.
LIMITEXCEEDED_MODULESECURITYGROUPLIMITEXCEEDED = 'LimitExceeded.ModuleSecurityGroupLimitExceeded'

# The number of ENIs or public IPs exceeds the limit specified by the CPU.
LIMITEXCEEDED_NICORIPLIMITEXCEEDED = 'LimitExceeded.NicOrIPLimitExceeded'

# The number of private IPs exceeds the limit.
LIMITEXCEEDED_PRIVATEIPQUOTALIMITEXCEEDED = 'LimitExceeded.PrivateIPQuotaLimitExceeded'

# The number of instances bound to the security group exceeds the limit.
LIMITEXCEEDED_SECURITYGROUPINSTANCELIMITEXCEEDED = 'LimitExceeded.SecurityGroupInstanceLimitExceeded'

# The number of modules that can be associated with the security group exceeds the limit.
LIMITEXCEEDED_SECURITYGROUPMODULELIMITEXCEEDED = 'LimitExceeded.SecurityGroupModuleLimitExceeded'

# The number of security group rules exceeds the upper limit.
LIMITEXCEEDED_SECURITYGROUPPOLICYSET = 'LimitExceeded.SecurityGroupPolicySet'

# The number of CPU cores applied for exceeds the limit.
LIMITEXCEEDED_VCPULIMITEXCEEDED = 'LimitExceeded.VcpuLimitExceeded'

# The parameter is missing.
MISSINGPARAMETER = 'MissingParameter'

# The entity parameter to be associated is missing.
MISSINGPARAMETER_MISSINGASSOCIATEENTITY = 'MissingParameter.MissingAssociateEntity'

# The request parameters required to get the basic configuration are incomplete.
MISSINGPARAMETER_MISSINGBASECONFIGPARAMETER = 'MissingParameter.MissingBaseConfigParameter'

# The image operation parameters are incomplete.
MISSINGPARAMETER_MISSINGIMAGEPARAMETER = 'MissingParameter.MissingImageParameter'

# The model operation parameters are incomplete.
MISSINGPARAMETER_MISSINGINSTANCETYPECONFIGPARAMETER = 'MissingParameter.MissingInstanceTypeConfigParameter'

# The instance operation parameters are incomplete.
MISSINGPARAMETER_MISSINGINSTANCESPARAMETER = 'MissingParameter.MissingInstancesParameter'

# The module operation parameters are incomplete.
MISSINGPARAMETER_MISSINGMODULEPARAMETER = 'MissingParameter.MissingModuleParameter'

# The request parameters required for ENI operation configuration are missing.
MISSINGPARAMETER_MISSINGNETWORKINTERFACEPARAMETER = 'MissingParameter.MissingNetworkInterfaceParameter'

# The node operation parameters are incomplete.
MISSINGPARAMETER_MISSINGNODEPARAMETER = 'MissingParameter.MissingNodeParameter'

# The request parameters required to get the configuration of the overview page are incomplete.
MISSINGPARAMETER_MISSINGOVERVIEWPARAMETER = 'MissingParameter.MissingOverViewParameter'

# The private IP address is missing.
MISSINGPARAMETER_MISSINGPRIVATEIPADDRESS = 'MissingParameter.MissingPrivateIpAddress'

# The current operation is not allowed.
OPERATIONDENIED_INSTANCEOPERATIONINPROGRESS = 'OperationDenied.InstanceOperationInProgress'

# The resource is in use.
RESOURCEINUSE = 'ResourceInUse'

# Insufficient resource.
RESOURCEINSUFFICIENT = 'ResourceInsufficient'

# Insufficient IP resource.
RESOURCEINSUFFICIENT_IPQUOTANOTENOUGH = 'ResourceInsufficient.IPQuotaNotEnough'

# The instance resource is insufficient.
RESOURCEINSUFFICIENT_INSTANCEQUOTANOTENOUGH = 'ResourceInsufficient.InstanceQuotaNotEnough'

# The number of private images exceeds the limit.
RESOURCEINSUFFICIENT_INVAILDPRIVATEIMAGENUM = 'ResourceInsufficient.InvaildPrivateImageNum'

# 
RESOURCEINSUFFICIENT_PRIVATEIPQUOTANOTENOUGH = 'ResourceInsufficient.PrivateIPQuotaNotEnough'

# The resource does not exist.
RESOURCENOTFOUND = 'ResourceNotFound'

# The instance is invalid.
RESOURCENOTFOUND_INSTANCENOTEXIST = 'ResourceNotFound.InstanceNotExist'

# The instance is not running.
RESOURCEUNAVAILABLE_INSTANCENOTRUNNING = 'ResourceUnavailable.InstanceNotRunning'

# CLB instances have been sold out.
RESOURCESSOLDOUT_LOADBALANCERSOLDOUT = 'ResourcesSoldOut.LoadBalancerSoldOut'

# 
RESOURCESSOLDOUT_SPECIFIEDINSTANCETYPE = 'ResourcesSoldOut.SpecifiedInstanceType'

# You don't have the permission to perform this operation.
UNAUTHORIZEDOPERATION_FORBIDDENOPERATION = 'UnauthorizedOperation.ForbiddenOperation'

# UnauthorizedOperation.MFAExpired
UNAUTHORIZEDOPERATION_MFAEXPIRED = 'UnauthorizedOperation.MFAExpired'

# Unsupported operation.
UNSUPPORTEDOPERATION = 'UnsupportedOperation'

# The IP was not found.
UNSUPPORTEDOPERATION_ADDRESSIDNOTFOUND = 'UnsupportedOperation.AddressIdNotFound'

# The specified instance has been bound to an EIP. You must unbind it from the current EIP first before you can bind it to another EIP.
UNSUPPORTEDOPERATION_ALREADYBINDEIP = 'UnsupportedOperation.AlreadyBindEip'

# The ENI is already associated with an instance.
UNSUPPORTEDOPERATION_ATTACHMENTALREADYEXISTS = 'UnsupportedOperation.AttachmentAlreadyExists'

# The instance is not associated.
UNSUPPORTEDOPERATION_ATTACHMENTNOTFOUND = 'UnsupportedOperation.AttachmentNotFound'

# The default route table cannot be deleted.
UNSUPPORTEDOPERATION_DELDEFAULTROUTE = 'UnsupportedOperation.DelDefaultRoute'

# The route table associated with a subnet cannot be deleted.
UNSUPPORTEDOPERATION_DELROUTEWITHSUBNET = 'UnsupportedOperation.DelRouteWithSubnet'

# The security group policy is duplicate.
UNSUPPORTEDOPERATION_DUPLICATEPOLICY = 'UnsupportedOperation.DuplicatePolicy'

# The ECMP is not supported.
UNSUPPORTEDOPERATION_ECMP = 'UnsupportedOperation.Ecmp'

# ECMP was formed with the CCN route.
UNSUPPORTEDOPERATION_ECMPWITHCCNROUTE = 'UnsupportedOperation.EcmpWithCcnRoute'

# ECMP was formed with the custom route.
UNSUPPORTEDOPERATION_ECMPWITHUSERROUTE = 'UnsupportedOperation.EcmpWithUserRoute'

# The instance ID is invalid, as the specified instance ID does not exist.
UNSUPPORTEDOPERATION_INSTANCEIDNOTFOUND = 'UnsupportedOperation.InstanceIdNotFound'

# The instance is not supported.
UNSUPPORTEDOPERATION_INSTANCEIDNOTSUPPORTED = 'UnsupportedOperation.InstanceIdNotSupported'

# The current model does not support the selected image.
UNSUPPORTEDOPERATION_INSTANCETYPENOTSUPPORTIMAGE = 'UnsupportedOperation.InstanceTypeNotSupportImage'

# This operation cannot be performed in the current status.
UNSUPPORTEDOPERATION_INVALIDINSTANCESTATE = 'UnsupportedOperation.InvalidInstanceState'

# The specified `NetworkInterfaceId` does not exist, or the specified `PrivateIpAddress` is not on the `NetworkInterfaceId`.
UNSUPPORTEDOPERATION_INVALIDNETWORKINTERFACEIDNOTFOUND = 'UnsupportedOperation.InvalidNetworkInterfaceIdNotFound'

# The specified private IP of the specified ENI has already been bound to an EIP. A private IP cannot be bound to more than one EIP.
UNSUPPORTEDOPERATION_INVALIDPRIVATEIPADDRESSALREADYBINDEIP = 'UnsupportedOperation.InvalidPrivateIpAddressAlreadyBindEip'

# The resource status is invalid.
UNSUPPORTEDOPERATION_INVALIDSTATE = 'UnsupportedOperation.InvalidState'

# Please check whether the provided IP address is complete.
UNSUPPORTEDOPERATION_MALFORMED = 'UnsupportedOperation.Malformed'

# A task with a mutually exclusive resource is being executed.
UNSUPPORTEDOPERATION_MUTEXOPERATIONTASKRUNNING = 'UnsupportedOperation.MutexOperationTaskRunning'

# The instance specification supports binding only three EIPs.
UNSUPPORTEDOPERATION_QUOTALIMITEXCEEDED = 'UnsupportedOperation.QuotaLimitExceeded'

# UnsupportedOperation.SnapHasShared
UNSUPPORTEDOPERATION_SNAPHASSHARED = 'UnsupportedOperation.SnapHasShared'

# UnsupportedOperation.SnapshotHasBindedImage
UNSUPPORTEDOPERATION_SNAPSHOTHASBINDEDIMAGE = 'UnsupportedOperation.SnapshotHasBindedImage'

# This operation cannot be performed in the current status.
UNSUPPORTEDOPERATION_STATUSNOTPERMIT = 'UnsupportedOperation.StatusNotPermit'

# Operations on the system route are prohibited.
UNSUPPORTEDOPERATION_SYSTEMROUTE = 'UnsupportedOperation.SystemRoute'

# The specified version number of the security group rule is inconsistent with the latest version.
UNSUPPORTEDOPERATION_VERSIONMISMATCH = 'UnsupportedOperation.VersionMismatch'

# The resources are not in the same VPC.
UNSUPPORTEDOPERATION_VPCMISMATCH = 'UnsupportedOperation.VpcMismatch'
