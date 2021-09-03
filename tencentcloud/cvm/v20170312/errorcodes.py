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


# Your account failed the qualification verification.
ACCOUNTQUALIFICATIONRESTRICTIONS = 'AccountQualificationRestrictions'

# Role name authentication failed.
AUTHFAILURE_CAMROLENAMEAUTHENTICATEFAILED = 'AuthFailure.CamRoleNameAuthenticateFailed'

# ENIs do not support changing subnets.
ENINOTALLOWEDCHANGESUBNET = 'EniNotAllowedChangeSubnet'

# The account already exists.
FAILEDOPERATION_ACCOUNTALREADYEXISTS = 'FailedOperation.AccountAlreadyExists'

# You cannot share images with yourself.
FAILEDOPERATION_ACCOUNTISYOURSELF = 'FailedOperation.AccountIsYourSelf'

# The specified spread placement group does not exist.
FAILEDOPERATION_DISASTERRECOVERGROUPNOTFOUND = 'FailedOperation.DisasterRecoverGroupNotFound'

# The tag key contains invalid characters.
FAILEDOPERATION_ILLEGALTAGKEY = 'FailedOperation.IllegalTagKey'

# The tag value contains invalid characters.
FAILEDOPERATION_ILLEGALTAGVALUE = 'FailedOperation.IllegalTagValue'

# Price query failed.
FAILEDOPERATION_INQUIRYPRICEFAILED = 'FailedOperation.InquiryPriceFailed'

# Failed to query the refund: the payment order is not found. Check whether the instance `ins-xxxxxxx` has expired.
FAILEDOPERATION_INQUIRYREFUNDPRICEFAILED = 'FailedOperation.InquiryRefundPriceFailed'

# The EMR instance `ins-xxxxxxxx` does not support this operation.
FAILEDOPERATION_INVALIDINSTANCEAPPLICATIONROLEEMR = 'FailedOperation.InvalidInstanceApplicationRoleEmr'

# This instance does not bind an EIP.
FAILEDOPERATION_NOTFOUNDEIP = 'FailedOperation.NotFoundEIP'

# You’re using a collaborator account. Please enter a root account.
FAILEDOPERATION_NOTMASTERACCOUNT = 'FailedOperation.NotMasterAccount'

# The specified placement group is not empty.
FAILEDOPERATION_PLACEMENTSETNOTEMPTY = 'FailedOperation.PlacementSetNotEmpty'

# The configuration or billing mode of the CVM instances purchased during the promotion period cannot be modified.
FAILEDOPERATION_PROMOTIONALPERIORESTRICTION = 'FailedOperation.PromotionalPerioRestriction'

# Image sharing failed.
FAILEDOPERATION_QIMAGESHAREFAILED = 'FailedOperation.QImageShareFailed'

# Image sharing failed.
FAILEDOPERATION_RIMAGESHAREFAILED = 'FailedOperation.RImageShareFailed'

# Security group operation failed.
FAILEDOPERATION_SECURITYGROUPACTIONFAILED = 'FailedOperation.SecurityGroupActionFailed'

# The snapshot size is larger than the disk capacity. You need a larger disk space.
FAILEDOPERATION_SNAPSHOTSIZELARGERTHANDATASIZE = 'FailedOperation.SnapshotSizeLargerThanDataSize'

# The snapshot size should be larger than the cloud disk capacity.
FAILEDOPERATION_SNAPSHOTSIZELESSTHANDATASIZE = 'FailedOperation.SnapshotSizeLessThanDataSize'

# The tag key specified in the request is reserved for the system.
FAILEDOPERATION_TAGKEYRESERVED = 'FailedOperation.TagKeyReserved'

# This image is not a Linux&x86_64 image.
FAILEDOPERATION_TATAGENTNOTSUPPORT = 'FailedOperation.TatAgentNotSupport'

# The instance is unreturnable.
FAILEDOPERATION_UNRETURNABLE = 'FailedOperation.Unreturnable'

# The image quota has been exceeded.
IMAGEQUOTALIMITEXCEEDED = 'ImageQuotaLimitExceeded'

# You are trying to create more instances than your remaining quota allows.
INSTANCESQUOTALIMITEXCEEDED = 'InstancesQuotaLimitExceeded'

# Internal error.
INTERNALERROR_TRADEUNKNOWNERROR = 'InternalError.TradeUnknownError'

# Internal error.
INTERNALSERVERERROR = 'InternalServerError'

# Insufficient account balance.
INVALIDACCOUNT_INSUFFICIENTBALANCE = 'InvalidAccount.InsufficientBalance'

# The account has unpaid orders.
INVALIDACCOUNT_UNPAIDORDER = 'InvalidAccount.UnpaidOrder'

# Invalid account ID.
INVALIDACCOUNTID_NOTFOUND = 'InvalidAccountId.NotFound'

# You cannot share images with yourself.
INVALIDACCOUNTIS_YOURSELF = 'InvalidAccountIs.YourSelf'

# The specified ClientToken exceeds the maximum length of 64 bytes.
INVALIDCLIENTTOKEN_TOOLONG = 'InvalidClientToken.TooLong'

# Invalid filter.
INVALIDFILTER = 'InvalidFilter'

# [`Filter`](https://intl.cloud.tencent.com/document/api/213/15753?from_cn_redirect=1#Filter)
INVALIDFILTERVALUE_LIMITEXCEEDED = 'InvalidFilterValue.LimitExceeded'

# The specified operation on this CDH instance is not support .
INVALIDHOST_NOTSUPPORTED = 'InvalidHost.NotSupported'

# Invalid [CDH](https://intl.cloud.tencent.com/document/product/416?from_cn_redirect=1) `ID`. The specified [CDH](https://intl.cloud.tencent.com/document/product/416?from_cn_redirect=1) `ID` has an invalid format. For example, `host-1122` has an invalid `ID` length.
INVALIDHOSTID_MALFORMED = 'InvalidHostId.Malformed'

# The specified HostId does not exist, or does not belong to your account.
INVALIDHOSTID_NOTFOUND = 'InvalidHostId.NotFound'

# The image is being shared.
INVALIDIMAGEID_INSHARED = 'InvalidImageId.InShared'

# Invalid image status.
INVALIDIMAGEID_INCORRECTSTATE = 'InvalidImageId.IncorrectState'

# Invalid image ID format.
INVALIDIMAGEID_MALFORMED = 'InvalidImageId.Malformed'

# The image cannot be found.
INVALIDIMAGEID_NOTFOUND = 'InvalidImageId.NotFound'

# The image size exceeds the limit.
INVALIDIMAGEID_TOOLARGE = 'InvalidImageId.TooLarge'

# The specified image name already exists.
INVALIDIMAGENAME_DUPLICATE = 'InvalidImageName.Duplicate'

# The operating system type is not supported.
INVALIDIMAGEOSTYPE_UNSUPPORTED = 'InvalidImageOsType.Unsupported'

# The operating system version is not supported.
INVALIDIMAGEOSVERSION_UNSUPPORTED = 'InvalidImageOsVersion.Unsupported'

# This instance is not supported.
INVALIDINSTANCE_NOTSUPPORTED = 'InvalidInstance.NotSupported'

# Invalid instance `ID`. The specified instance `ID` has an invalid format. For example, `ins-1122` has an invalid `ID` length.
INVALIDINSTANCEID_MALFORMED = 'InvalidInstanceId.Malformed'

# No instance found.
INVALIDINSTANCEID_NOTFOUND = 'InvalidInstanceId.NotFound'

# The specified InstanceName exceeds the maximum length of 60 bytes.
INVALIDINSTANCENAME_TOOLONG = 'InvalidInstanceName.TooLong'

# This instance does not meet the [Return Policy](https://intl.cloud.tencent.com/document/product/213/9711?from_cn_redirect=1) for prepaid instances.
INVALIDINSTANCENOTSUPPORTEDPREPAIDINSTANCE = 'InvalidInstanceNotSupportedPrepaidInstance'

# This operation cannot be performed due to the current instance status.
INVALIDINSTANCESTATE = 'InvalidInstanceState'

# The specified `InstanceType` parameter has an invalid format.
INVALIDINSTANCETYPE_MALFORMED = 'InvalidInstanceType.Malformed'

# The number of key pairs exceeds the limit.
INVALIDKEYPAIR_LIMITEXCEEDED = 'InvalidKeyPair.LimitExceeded'

# Invalid key pair ID. The specified key pair ID has an invalid format. For example, `skey-1122` has an invalid `ID` length.
INVALIDKEYPAIRID_MALFORMED = 'InvalidKeyPairId.Malformed'

# Invalid key pair ID. The specified key pair ID does not exist.
INVALIDKEYPAIRID_NOTFOUND = 'InvalidKeyPairId.NotFound'

# Key pair name already exists.
INVALIDKEYPAIRNAME_DUPLICATE = 'InvalidKeyPairName.Duplicate'

# The key name cannot be empty.
INVALIDKEYPAIRNAMEEMPTY = 'InvalidKeyPairNameEmpty'

# The key name contains invalid characters. Key names can only contain letters, numbers and underscores.
INVALIDKEYPAIRNAMEINCLUDEILLEGALCHAR = 'InvalidKeyPairNameIncludeIllegalChar'

# The key name cannot exceed 25 characters.
INVALIDKEYPAIRNAMETOOLONG = 'InvalidKeyPairNameTooLong'

# A parameter error occurred.
INVALIDPARAMETER = 'InvalidParameter'

# RootDisk ID should not be passed to DataDiskIds.
INVALIDPARAMETER_DATADISKIDCONTAINSROOTDISK = 'InvalidParameter.DataDiskIdContainsRootDisk'

# The specified data disk does not belong to the specified instance.
INVALIDPARAMETER_DATADISKNOTBELONGSPECIFIEDINSTANCE = 'InvalidParameter.DataDiskNotBelongSpecifiedInstance'

# Only one system disk snapshot can be included.
INVALIDPARAMETER_DUPLICATESYSTEMSNAPSHOTS = 'InvalidParameter.DuplicateSystemSnapshots'

# The specified HostName is invalid.
INVALIDPARAMETER_HOSTNAMEILLEGAL = 'InvalidParameter.HostNameIllegal'

# This API does not support instance images.
INVALIDPARAMETER_INSTANCEIMAGENOTSUPPORT = 'InvalidParameter.InstanceImageNotSupport'

# Invalid parameter dependency.
INVALIDPARAMETER_INVALIDDEPENDENCE = 'InvalidParameter.InvalidDependence'

# Invalid VPC IP address format.
INVALIDPARAMETER_INVALIDIPFORMAT = 'InvalidParameter.InvalidIpFormat'

# `ImageIds` and `Filters` cannot be specified at the same time.
INVALIDPARAMETER_INVALIDPARAMETERCOEXISTIMAGEIDSFILTERS = 'InvalidParameter.InvalidParameterCoexistImageIdsFilters'

# Invalid URL.
INVALIDPARAMETER_INVALIDPARAMETERURLERROR = 'InvalidParameter.InvalidParameterUrlError'

# `CoreCount` and `ThreadPerCore` must be specified at the same time.
INVALIDPARAMETER_LACKCORECOUNTORTHREADPERCORE = 'InvalidParameter.LackCoreCountOrThreadPerCore'

# Local data disks cannot be used to create instance images.
INVALIDPARAMETER_LOCALDATADISKNOTSUPPORT = 'InvalidParameter.LocalDataDiskNotSupport'

# Specifying an SSH key will override the original one of the image.
INVALIDPARAMETER_PARAMETERCONFLICT = 'InvalidParameter.ParameterConflict'

# The specified snapshot does not exist.
INVALIDPARAMETER_SNAPSHOTNOTFOUND = 'InvalidParameter.SnapshotNotFound'

# At least one of the multiple parameters must be passed in.
INVALIDPARAMETER_SPECIFYONEPARAMETER = 'InvalidParameter.SpecifyOneParameter'

# Swap disks are not supported.
INVALIDPARAMETER_SWAPDISKNOTSUPPORT = 'InvalidParameter.SwapDiskNotSupport'

# The parameter does not contain system disk snapshot.
INVALIDPARAMETER_SYSTEMSNAPSHOTNOTFOUND = 'InvalidParameter.SystemSnapshotNotFound'

# The length of parameter exceeds the limit.
INVALIDPARAMETER_VALUETOOLARGE = 'InvalidParameter.ValueTooLarge'

# The parameter combination is invalid.
INVALIDPARAMETERCOMBINATION = 'InvalidParameterCombination'

# The two specified parameters conflict. An EIP can only be bound to the instance or the specified private IP of the specified ENI.
INVALIDPARAMETERCONFLICT = 'InvalidParameterConflict'

# Incorrect parameter value.
INVALIDPARAMETERVALUE = 'InvalidParameterValue'

# 
INVALIDPARAMETERVALUE_BANDWIDTHPACKAGEIDMALFORMED = 'InvalidParameterValue.BandwidthPackageIdMalformed'

# The specified bandwidth package does not exist.
INVALIDPARAMETERVALUE_BANDWIDTHPACKAGEIDNOTFOUND = 'InvalidParameterValue.BandwidthPackageIdNotFound'

# Corresponding CHC hosts not found
INVALIDPARAMETERVALUE_CHCHOSTSNOTFOUND = 'InvalidParameterValue.ChcHostsNotFound'

# The minimum capacity of a SSD data disk is 100 GB.
INVALIDPARAMETERVALUE_CLOUDSSDDATADISKSIZETOOSMALL = 'InvalidParameterValue.CloudSsdDataDiskSizeTooSmall'

# Illegal core count.
INVALIDPARAMETERVALUE_CORECOUNTVALUE = 'InvalidParameterValue.CoreCountValue'

# Duplicate parameter value
INVALIDPARAMETERVALUE_DUPLICATE = 'InvalidParameterValue.Duplicate'

# Non-GPU instances cannot be changed to the GPU instance.
INVALIDPARAMETERVALUE_GPUINSTANCEFAMILY = 'InvalidParameterValue.GPUInstanceFamily'

# Invalid IP format
INVALIDPARAMETERVALUE_IPADDRESSMALFORMED = 'InvalidParameterValue.IPAddressMalformed'

# Invalid IPv6 address
INVALIDPARAMETERVALUE_IPV6ADDRESSMALFORMED = 'InvalidParameterValue.IPv6AddressMalformed'

# The value of HostName is invalid.
INVALIDPARAMETERVALUE_ILLEGALHOSTNAME = 'InvalidParameterValue.IllegalHostName'

# The specified instance type does not exist.
INVALIDPARAMETERVALUE_INSTANCETYPENOTFOUND = 'InvalidParameterValue.InstanceTypeNotFound'

# This type of instances cannot be added to the HPC cluster.
INVALIDPARAMETERVALUE_INSTANCETYPENOTSUPPORTHPCCLUSTER = 'InvalidParameterValue.InstanceTypeNotSupportHpcCluster'

# The HPC cluster needs to be specified for the high-performance computing instance.
INVALIDPARAMETERVALUE_INSTANCETYPEREQUIREDHPCCLUSTER = 'InvalidParameterValue.InstanceTypeRequiredHpcCluster'

# The spot instance is out of stock.
INVALIDPARAMETERVALUE_INSUFFICIENTOFFERING = 'InvalidParameterValue.InsufficientOffering'

# The bid is lower than the market price.
INVALIDPARAMETERVALUE_INSUFFICIENTPRICE = 'InvalidParameterValue.InsufficientPrice'

# Invalid AppID
INVALIDPARAMETERVALUE_INVALIDAPPIDFORMAT = 'InvalidParameterValue.InvalidAppIdFormat'

# The specified image does not support the specified instance type.
INVALIDPARAMETERVALUE_INVALIDIMAGEFORGIVENINSTANCETYPE = 'InvalidParameterValue.InvalidImageForGivenInstanceType'

# A RAW image cannot be used to create a CVM. Choose another image.
INVALIDPARAMETERVALUE_INVALIDIMAGEFORMAT = 'InvalidParameterValue.InvalidImageFormat'

# The image does not support this operation.
INVALIDPARAMETERVALUE_INVALIDIMAGEID = 'InvalidParameterValue.InvalidImageId'

# The operating system of the specified image is not available in the current region.
INVALIDPARAMETERVALUE_INVALIDIMAGEOSNAME = 'InvalidParameterValue.InvalidImageOsName'

# The image has another ongoing task. Please check and try again later.
INVALIDPARAMETERVALUE_INVALIDIMAGESTATE = 'InvalidParameterValue.InvalidImageState'

# Invalid IP address.
INVALIDPARAMETERVALUE_INVALIDIPFORMAT = 'InvalidParameterValue.InvalidIpFormat'

# Invalid parameter value.
INVALIDPARAMETERVALUE_INVALIDPARAMETERVALUELIMIT = 'InvalidParameterValue.InvalidParameterValueLimit'

# Incorrect time format.
INVALIDPARAMETERVALUE_INVALIDTIMEFORMAT = 'InvalidParameterValue.InvalidTimeFormat'

# Incorrect UserData format. Use the Base64-encoded format.
INVALIDPARAMETERVALUE_INVALIDUSERDATAFORMAT = 'InvalidParameterValue.InvalidUserDataFormat'

# Invalid fuzzy query string
INVALIDPARAMETERVALUE_INVALIDVAGUENAME = 'InvalidParameterValue.InvalidVagueName'

# The key does not exist.
INVALIDPARAMETERVALUE_KEYPAIRNOTFOUND = 'InvalidParameterValue.KeyPairNotFound'

# The specified key does not support the operation.
INVALIDPARAMETERVALUE_KEYPAIRNOTSUPPORTED = 'InvalidParameterValue.KeyPairNotSupported'

# The instance launch template ID does not exist.
INVALIDPARAMETERVALUE_LAUNCHTEMPLATEIDNOTEXISTED = 'InvalidParameterValue.LaunchTemplateIdNotExisted'

# The number of parameter values exceeds the limit.
INVALIDPARAMETERVALUE_LIMITEXCEEDED = 'InvalidParameterValue.LimitExceeded'

# The parameter value must be a DHCP-enabled VPC.
INVALIDPARAMETERVALUE_MUSTDHCPENABLEDVPC = 'InvalidParameterValue.MustDhcpEnabledVpc'

# Unsupported operation.
INVALIDPARAMETERVALUE_NOTSUPPORTED = 'InvalidParameterValue.NotSupported'

#  Invalid parameter value: invalid parameter value range.
INVALIDPARAMETERVALUE_RANGE = 'InvalidParameterValue.Range'

# Invalid snapshot ID. Provide a snapshot ID in the format of snap-xxxxxxxx, where the letter x refers to lowercase letter or number.
INVALIDPARAMETERVALUE_SNAPSHOTIDMALFORMED = 'InvalidParameterValue.SnapshotIdMalformed'

# Invalid subnet ID. Please provide a subnet ID in the format of subnet-xxxxxxxx, where “x” can be a lowercase letter or number.
INVALIDPARAMETERVALUE_SUBNETIDMALFORMED = 'InvalidParameterValue.SubnetIdMalformed'

# Creation failed: the subnet does not exist. Please specify another subnet.
INVALIDPARAMETERVALUE_SUBNETNOTEXIST = 'InvalidParameterValue.SubnetNotExist'

# The specified tag does not exist
INVALIDPARAMETERVALUE_TAGKEYNOTFOUND = 'InvalidParameterValue.TagKeyNotFound'

# Invalid thread count per core.
INVALIDPARAMETERVALUE_THREADPERCOREVALUE = 'InvalidParameterValue.ThreadPerCoreValue'

# The parameter value exceeds the maximum limit.
INVALIDPARAMETERVALUE_TOOLARGE = 'InvalidParameterValue.TooLarge'

# Invalid parameter value: parameter value is too long.
INVALIDPARAMETERVALUE_TOOLONG = 'InvalidParameterValue.TooLong'

# The VPC ID `xxx` is invalid. Please provide a VPC ID in the format of vpc-xxxxxxxx, where “x” can be a lowercase letter or number.
INVALIDPARAMETERVALUE_VPCIDMALFORMED = 'InvalidParameterValue.VpcIdMalformed'

# The VPC and instance must be in the same availability zone.
INVALIDPARAMETERVALUE_VPCIDZONEIDNOTMATCH = 'InvalidParameterValue.VpcIdZoneIdNotMatch'

# The availability zone does not support this operation.
INVALIDPARAMETERVALUE_ZONENOTSUPPORTED = 'InvalidParameterValue.ZoneNotSupported'

# The number of parameter values exceeds the limit.
INVALIDPARAMETERVALUELIMIT = 'InvalidParameterValueLimit'

# Invalid parameter value: invalid `Offset`.
INVALIDPARAMETERVALUEOFFSET = 'InvalidParameterValueOffset'

# Invalid password. The specified password does not meet the password requirements. For example, the password length does not meet the requirements.
INVALIDPASSWORD = 'InvalidPassword'

# Invalid period. Valid values: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 24, 36]; unit: month.
INVALIDPERIOD = 'InvalidPeriod'

# This operation is not supported for the account.
INVALIDPERMISSION = 'InvalidPermission'

# Invalid project ID: the specified project ID does not exist.
INVALIDPROJECTID_NOTFOUND = 'InvalidProjectId.NotFound'

# Invalid public key: the specified key already exists.
INVALIDPUBLICKEY_DUPLICATE = 'InvalidPublicKey.Duplicate'

# Invalid public key: the specified public key does not meet the `OpenSSH RSA` format requirements.
INVALIDPUBLICKEY_MALFORMED = 'InvalidPublicKey.Malformed'

# The region cannot be found.
INVALIDREGION_NOTFOUND = 'InvalidRegion.NotFound'

# Currently this region does not support image synchronization.
INVALIDREGION_UNAVAILABLE = 'InvalidRegion.Unavailable'

# The specified `security group ID` does not exist.
INVALIDSECURITYGROUPID_NOTFOUND = 'InvalidSecurityGroupId.NotFound'

# The specified `security group ID` is in the wrong format. For example, `sg-ide32` has an invalid `instance ID` length.
INVALIDSGID_MALFORMED = 'InvalidSgId.Malformed'

# The specified `zone` does not exist.
INVALIDZONE_MISMATCHREGION = 'InvalidZone.MismatchRegion'

# An instance can be bound with up to 5 security groups.
LIMITEXCEEDED_ASSOCIATEUSGLIMITEXCEEDED = 'LimitExceeded.AssociateUSGLimitExceeded'

# The CVM ENIs associated with the security group has exceeded the limit.
LIMITEXCEEDED_CVMSVIFSPERSECGROUPLIMITEXCEEDED = 'LimitExceeded.CvmsVifsPerSecGroupLimitExceeded'

# The quota of the specified placement group is insufficient.
LIMITEXCEEDED_DISASTERRECOVERGROUP = 'LimitExceeded.DisasterRecoverGroup'

# The number of ENIs on a specified instance exceeds the maximum ENIs allowed for the target instance type. Delete some ENIs and try again.
LIMITEXCEEDED_ENINUMLIMIT = 'LimitExceeded.EniNumLimit'

# Number of IPs on this ENI reached the upper limit
LIMITEXCEEDED_IPV6ADDRESSNUM = 'LimitExceeded.IPv6AddressNum'

# You are short of the instance quota.
LIMITEXCEEDED_INSTANCEQUOTA = 'LimitExceeded.InstanceQuota'

# Unable to adjust: the target instance type does not support the configured public network bandwidth cap. See [Public Network Bandwidth Cap](https://intl.cloud.tencent.com/document/product/213/12523).
LIMITEXCEEDED_INSTANCETYPEBANDWIDTH = 'LimitExceeded.InstanceTypeBandwidth'

# Your quota for monthly-subscribed instances is full. Increase your quota and try again.
LIMITEXCEEDED_PREPAYQUOTA = 'LimitExceeded.PrepayQuota'

# The number of security groups exceeds the quota limit.
LIMITEXCEEDED_SINGLEUSGQUOTA = 'LimitExceeded.SingleUSGQuota'

# The spot instance offerings are out of stock.
LIMITEXCEEDED_SPOTQUOTA = 'LimitExceeded.SpotQuota'

# Failed to return instances because of the quota limit.
LIMITEXCEEDED_USERRETURNQUOTA = 'LimitExceeded.UserReturnQuota'

# You are short of the spot instance quota.
LIMITEXCEEDED_USERSPOTQUOTA = 'LimitExceeded.UserSpotQuota'

# Insufficient subnet IPs.
LIMITEXCEEDED_VPCSUBNETNUM = 'LimitExceeded.VpcSubnetNum'

# Missing parameter.
MISSINGPARAMETER = 'MissingParameter'

# Parameter missing. Provide at least one parameter.
MISSINGPARAMETER_ATLEASTONE = 'MissingParameter.AtLeastOne'

# The DPDK instance requires a VPC.
MISSINGPARAMETER_DPDKINSTANCETYPEREQUIREDVPC = 'MissingParameter.DPDKInstanceTypeRequiredVPC'

# The instance type must have Cloud Monitor enabled.
MISSINGPARAMETER_MONITORSERVICE = 'MissingParameter.MonitorService'

# An identical job is running.
MUTEXOPERATION_TASKRUNNING = 'MutexOperation.TaskRunning'

# The instance has an operation in progress. Please try again later.
OPERATIONDENIED_INSTANCEOPERATIONINPROGRESS = 'OperationDenied.InstanceOperationInProgress'

# The number of shared images exceeds the quota.
OVERQUOTA = 'OverQuota'

# This region does not support importing images.
REGIONABILITYLIMIT_UNSUPPORTEDTOIMPORTIMAGE = 'RegionAbilityLimit.UnsupportedToImportImage'

# The resource is in use.
RESOURCEINUSE = 'ResourceInUse'

# The availability zone has been sold out.
RESOURCEINSUFFICIENT_AVAILABILITYZONESOLDOUT = 'ResourceInsufficient.AvailabilityZoneSoldOut'

# The specified cloud disk has been sold out.
RESOURCEINSUFFICIENT_CLOUDDISKSOLDOUT = 'ResourceInsufficient.CloudDiskSoldOut'

# The parameters of cloud disk do not meet the specification.
RESOURCEINSUFFICIENT_CLOUDDISKUNAVAILABLE = 'ResourceInsufficient.CloudDiskUnavailable'

# The number of instances exceeded the quota limit of spread placement groups.
RESOURCEINSUFFICIENT_DISASTERRECOVERGROUPCVMQUOTA = 'ResourceInsufficient.DisasterRecoverGroupCvmQuota'

# The specified instance type is insufficient.
RESOURCEINSUFFICIENT_SPECIFIEDINSTANCETYPE = 'ResourceInsufficient.SpecifiedInstanceType'

# The HPC cluster does not exist.
RESOURCENOTFOUND_HPCCLUSTER = 'ResourceNotFound.HpcCluster'

# The specified placement group does not exist.
RESOURCENOTFOUND_INVALIDPLACEMENTSET = 'ResourceNotFound.InvalidPlacementSet'

# No default CBS resources are available.
RESOURCENOTFOUND_NODEFAULTCBS = 'ResourceNotFound.NoDefaultCbs'

# No default CBS resources are available.
RESOURCENOTFOUND_NODEFAULTCBSWITHREASON = 'ResourceNotFound.NoDefaultCbsWithReason'

# This instance type is unavailable in the availability zone.
RESOURCEUNAVAILABLE_INSTANCETYPE = 'ResourceUnavailable.InstanceType'

# The snapshot is being created.
RESOURCEUNAVAILABLE_SNAPSHOTCREATING = 'ResourceUnavailable.SnapshotCreating'

# Resources in this availability zone has been sold out.
RESOURCESSOLDOUT_AVAILABLEZONE = 'ResourcesSoldOut.AvailableZone'

# The public IP has been sold out.
RESOURCESSOLDOUT_EIPINSUFFICIENT = 'ResourcesSoldOut.EipInsufficient'

# The specified instance type is sold out.
RESOURCESSOLDOUT_SPECIFIEDINSTANCETYPE = 'ResourcesSoldOut.SpecifiedInstanceType'

# A general error occurred during the security group service API call.
SECGROUPACTIONFAILURE = 'SecGroupActionFailure'

# 
UNAUTHORIZEDOPERATION = 'UnauthorizedOperation'

# The specified image does not belong to the user.
UNAUTHORIZEDOPERATION_IMAGENOTBELONGTOACCOUNT = 'UnauthorizedOperation.ImageNotBelongToAccount'

# Check if the token is valid.
UNAUTHORIZEDOPERATION_INVALIDTOKEN = 'UnauthorizedOperation.InvalidToken'

# Unauthorized operation. Make sure Multi-Factor Authentication (MFA) is valid.
UNAUTHORIZEDOPERATION_MFAEXPIRED = 'UnauthorizedOperation.MFAExpired'

# Unauthorized operation. Make sure Multi-Factor Authentication (MFA) exists.
UNAUTHORIZEDOPERATION_MFANOTFOUND = 'UnauthorizedOperation.MFANotFound'

# You’re not authorized for the operation. Please check the CAM policy.
UNAUTHORIZEDOPERATION_PERMISSIONDENIED = 'UnauthorizedOperation.PermissionDenied'

# The specified instance or network cannot use the bandwidth package.
UNSUPPORTEDOPERATION_BANDWIDTHPACKAGEIDNOTSUPPORTED = 'UnsupportedOperation.BandwidthPackageIdNotSupported'

# IPv6 instances cannot be migrated from Classiclink to VPC.
UNSUPPORTEDOPERATION_IPV6NOTSUPPORTVPCMIGRATE = 'UnsupportedOperation.IPv6NotSupportVpcMigrate'

# This instance billing mode does not support the operation.
UNSUPPORTEDOPERATION_INSTANCECHARGETYPE = 'UnsupportedOperation.InstanceChargeType'

# The instance `ins-xxxxxx` with the `Xserver windows2012cndatacenterx86_64` operating system does not support this operation.
UNSUPPORTEDOPERATION_INSTANCEOSWINDOWS = 'UnsupportedOperation.InstanceOsWindows'

# The instances are permanently corrupted, and this operation is not supported.
UNSUPPORTEDOPERATION_INSTANCESTATECORRUPTED = 'UnsupportedOperation.InstanceStateCorrupted'

# Instances are entering the rescue mode, and this operation is not supported.
UNSUPPORTEDOPERATION_INSTANCESTATEENTERRESCUEMODE = 'UnsupportedOperation.InstanceStateEnterRescueMode'

# The instance `ins-xxxxxx` in the `ENTER_SERVICE_LIVE_MIGRATE` status is not supported.
UNSUPPORTEDOPERATION_INSTANCESTATEENTERSERVICELIVEMIGRATE = 'UnsupportedOperation.InstanceStateEnterServiceLiveMigrate'

# Instances are exiting from the rescue mode, and this operation is not supported.
UNSUPPORTEDOPERATION_INSTANCESTATEEXITRESCUEMODE = 'UnsupportedOperation.InstanceStateExitRescueMode'

# The instance `ins-xxxxxx` in the `EXIT_SERVICE_LIVE_MIGRATE` status is not supported.
UNSUPPORTEDOPERATION_INSTANCESTATEEXITSERVICELIVEMIGRATE = 'UnsupportedOperation.InstanceStateExitServiceLiveMigrate'

# Unable to isolate: the instance is isolated
UNSUPPORTEDOPERATION_INSTANCESTATEISOLATING = 'UnsupportedOperation.InstanceStateIsolating'

# The instances are being created, and this operation is not supported.
UNSUPPORTEDOPERATION_INSTANCESTATEPENDING = 'UnsupportedOperation.InstanceStatePending'

# The instances are being restarted, and this operation is not supported.
UNSUPPORTEDOPERATION_INSTANCESTATEREBOOTING = 'UnsupportedOperation.InstanceStateRebooting'

# Instances in the rescue mode are not available for this operation.
UNSUPPORTEDOPERATION_INSTANCESTATERESCUEMODE = 'UnsupportedOperation.InstanceStateRescueMode'

# Running instances do not support this operation.
UNSUPPORTEDOPERATION_INSTANCESTATERUNNING = 'UnsupportedOperation.InstanceStateRunning'

# The instances are being migrated, and this operation is not supported.
UNSUPPORTEDOPERATION_INSTANCESTATESERVICELIVEMIGRATE = 'UnsupportedOperation.InstanceStateServiceLiveMigrate'

# Isolated instances do not support this operation.
UNSUPPORTEDOPERATION_INSTANCESTATESHUTDOWN = 'UnsupportedOperation.InstanceStateShutdown'

# The instance is starting up, and this operation is not supported.
UNSUPPORTEDOPERATION_INSTANCESTATESTARTING = 'UnsupportedOperation.InstanceStateStarting'

# The instance has been shut down, and this operation is not supported.
UNSUPPORTEDOPERATION_INSTANCESTATESTOPPED = 'UnsupportedOperation.InstanceStateStopped'

# The instance is being shut down, and this operation is not supported.
UNSUPPORTEDOPERATION_INSTANCESTATESTOPPING = 'UnsupportedOperation.InstanceStateStopping'

# Terminated instances are not supported.
UNSUPPORTEDOPERATION_INSTANCESTATETERMINATED = 'UnsupportedOperation.InstanceStateTerminated'

# The instance is being terminated, and the operation is not supported.
UNSUPPORTEDOPERATION_INSTANCESTATETERMINATING = 'UnsupportedOperation.InstanceStateTerminating'

# The specified disk is not supported.
UNSUPPORTEDOPERATION_INVALIDDISK = 'UnsupportedOperation.InvalidDisk'

# The current operation is only supported for Tencent Cloud International users.
UNSUPPORTEDOPERATION_INVALIDPERMISSIONNONINTERNATIONALACCOUNT = 'UnsupportedOperation.InvalidPermissionNonInternationalAccount'

# Encrypted disks are not available in the selected regions.
UNSUPPORTEDOPERATION_INVALIDREGIONDISKENCRYPT = 'UnsupportedOperation.InvalidRegionDiskEncrypt'

# Key-pair login is not available to Windows instances.
UNSUPPORTEDOPERATION_KEYPAIRUNSUPPORTEDWINDOWS = 'UnsupportedOperation.KeyPairUnsupportedWindows'

# A model whose data disks are all local disks does not support cross-model configuration adjustment.
UNSUPPORTEDOPERATION_LOCALDATADISKCHANGEINSTANCEFAMILY = 'UnsupportedOperation.LocalDataDiskChangeInstanceFamily'

# An instance bound with CLB does not support modifying its VPC attributes.
UNSUPPORTEDOPERATION_MODIFYVPCWITHCLB = 'UnsupportedOperation.ModifyVPCWithCLB'

# This instance type does not support spot instances.
UNSUPPORTEDOPERATION_NOINSTANCETYPESUPPORTSPOT = 'UnsupportedOperation.NoInstanceTypeSupportSpot'

# The instance does not support this operation.
UNSUPPORTEDOPERATION_NOTSUPPORTINSTANCEIMAGE = 'UnsupportedOperation.NotSupportInstanceImage'

# Only a prepaid account supports this operation.
UNSUPPORTEDOPERATION_ONLYFORPREPAIDACCOUNT = 'UnsupportedOperation.OnlyForPrepaidAccount'

# This image does not support instance reinstallation.
UNSUPPORTEDOPERATION_RAWLOCALDISKINSREINSTALLTOQCOW2 = 'UnsupportedOperation.RawLocalDiskInsReinstalltoQcow2'

# The region is unsupported.
UNSUPPORTEDOPERATION_REGION = 'UnsupportedOperation.Region'

# Purchasing reserved instances is not supported for the current user.
UNSUPPORTEDOPERATION_RESERVEDINSTANCEINVISIBLEFORUSER = 'UnsupportedOperation.ReservedInstanceInvisibleForUser'

# You’ve used up your quota for Reserved Instances.
UNSUPPORTEDOPERATION_RESERVEDINSTANCEOUTOFQUATA = 'UnsupportedOperation.ReservedInstanceOutofQuata'

# This special instance type does not support the operation.
UNSUPPORTEDOPERATION_SPECIALINSTANCETYPE = 'UnsupportedOperation.SpecialInstanceType'

# The instance does not support the **no charges when shut down** feature.
UNSUPPORTEDOPERATION_STOPPEDMODESTOPCHARGING = 'UnsupportedOperation.StoppedModeStopCharging'

# The specified model does not support cross-model configuration adjustment.
UNSUPPORTEDOPERATION_UNSUPPORTEDCHANGEINSTANCEFAMILY = 'UnsupportedOperation.UnsupportedChangeInstanceFamily'

# Non-ARM model instances cannot be changed to the ARM model.
UNSUPPORTEDOPERATION_UNSUPPORTEDCHANGEINSTANCEFAMILYTOARM = 'UnsupportedOperation.UnsupportedChangeInstanceFamilyToARM'

# The target model (SA3) does not support configuration adjustment.
UNSUPPORTEDOPERATION_UNSUPPORTEDCHANGEINSTANCEFAMILYTOSA3 = 'UnsupportedOperation.UnsupportedChangeInstanceFamilyToSA3'

# A Tencent Cloud International account does not support this operation.
UNSUPPORTEDOPERATION_UNSUPPORTEDINTERNATIONALUSER = 'UnsupportedOperation.UnsupportedInternationalUser'

# The VPC IP address is not in the subnet.
VPCADDRNOTINSUBNET = 'VpcAddrNotInSubNet'

# The VPC IP address is already occupied.
VPCIPISUSED = 'VpcIpIsUsed'
