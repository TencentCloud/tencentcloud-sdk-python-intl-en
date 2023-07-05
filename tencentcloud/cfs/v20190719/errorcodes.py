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


# A CAM signature/authentication error occurred.
AUTHFAILURE = 'AuthFailure'

# Failed to get the CFS service role.
AUTHFAILURE_GETROLEFAILED = 'AuthFailure.GetRoleFailed'

# Request unauthorized.
AUTHFAILURE_UNAUTHORIZEDOPERATION = 'AuthFailure.UnauthorizedOperation'

# Operation failed.
FAILEDOPERATION = 'FailedOperation'

# Failed to bind the resource pack to the file system.
FAILEDOPERATION_BINDRESOURCEPKGFAILED = 'FailedOperation.BindResourcePkgFailed'

# The resource is being created.
FAILEDOPERATION_CLIENTTOKENINUSE = 'FailedOperation.ClientTokenInUse'

# There are mount targets on the file system.
FAILEDOPERATION_MOUNTTARGETEXISTS = 'FailedOperation.MountTargetExists'

# The permission group has been bound to a file system.
FAILEDOPERATION_PGROUPINUSE = 'FailedOperation.PgroupInUse'

# The permission group is being updated.
FAILEDOPERATION_PGROUPISUPDATING = 'FailedOperation.PgroupIsUpdating'

# The permission group has been associated with a legacy instance. Please unassociate it and try again.
FAILEDOPERATION_PGROUPLINKCFSV10 = 'FailedOperation.PgroupLinkCfsv10'

# Failed to unbind the resource tag.
FAILEDOPERATION_UNTAGRESOURCEFAILED = 'FailedOperation.UntagResourceFailed'

# Internal error.
INTERNALERROR = 'InternalError'

# Failed to create the file system.
INTERNALERROR_CREATEFSFAILED = 'InternalError.CreateFsFailed'

# Failed to get the payment status of the user.
INTERNALERROR_GETACCOUNTSTATUSFAILED = 'InternalError.GetAccountStatusFailed'

# Invalid parameter.
INVALIDPARAMETER = 'InvalidParameter'

# The snapshot policy was not found.
INVALIDPARAMETER_AUTOPOLICYNOTFOUND = 'InvalidParameter.AutoPolicyNotFound'

# The snapshot retention period is invalid.
INVALIDPARAMETER_INVALIDALIVEDDAYS = 'InvalidParameter.InvalidAlivedDays'

# The scheduled day of the week parameter is invalid.
INVALIDPARAMETER_INVALIDPARAMDAYOFWEEK = 'InvalidParameter.InvalidParamDayofWeek'

# The value of the scheduled hour parameter is incorrect.
INVALIDPARAMETER_INVALIDPARAMHOUR = 'InvalidParameter.InvalidParamHour'

# The snapshot policy is invalid.
INVALIDPARAMETER_INVALIDSNAPPOLICYSTATUS = 'InvalidParameter.InvalidSnapPolicyStatus'

# The file system snapshot parameter name is invalid.
INVALIDPARAMETER_INVALIDSNAPSHOTNAME = 'InvalidParameter.InvalidSnapshotName'

# The file system snapshot policy name is invalid.
INVALIDPARAMETER_INVALIDSNAPSHOTPOLICYNAME = 'InvalidParameter.InvalidSnapshotPolicyName'

# The policy parameter is missing.
INVALIDPARAMETER_MISSINGPOLICYPARAM = 'InvalidParameter.MissingPolicyParam'

# The file system snapshot name exceeds the upper limit.
INVALIDPARAMETER_SNAPSHOTNAMELIMITEXCEEDED = 'InvalidParameter.SnapshotNameLimitExceeded'

# The file system snapshot policy name exceeds the limit.
INVALIDPARAMETER_SNAPSHOTPOLICYNAMELIMITEXCEEDED = 'InvalidParameter.SnapshotPolicyNameLimitExceeded'

# The parameter value is incorrect.
INVALIDPARAMETERVALUE = 'InvalidParameterValue'

# 
INVALIDPARAMETERVALUE_AUTOPOLICYNOTFOUND = 'InvalidParameterValue.AutoPolicyNotFound'

# The length of the string used to ensure the idempotency of the request exceeds the upper limit of 64 bytes.
INVALIDPARAMETERVALUE_CLIENTTOKENLIMITEXCEEDED = 'InvalidParameterValue.ClientTokenLimitExceeded'

# The permission group name already exists.
INVALIDPARAMETERVALUE_DUPLICATEDPGROUPNAME = 'InvalidParameterValue.DuplicatedPgroupName'

# The rule IP already exists.
INVALIDPARAMETERVALUE_DUPLICATEDRULEAUTHCLIENTIP = 'InvalidParameterValue.DuplicatedRuleAuthClientIp'

# Duplicate tag key.
INVALIDPARAMETERVALUE_DUPLICATEDTAGKEY = 'InvalidParameterValue.DuplicatedTagKey'

# The length of the custom file system name exceeds the limit (64 bytes).
INVALIDPARAMETERVALUE_FSNAMELIMITEXCEEDED = 'InvalidParameterValue.FsNameLimitExceeded'

# The file system quota exceeds the upper limit.
INVALIDPARAMETERVALUE_FSSIZELIMITEXCEEDED = 'InvalidParameterValue.FsSizeLimitExceeded'

# 
INVALIDPARAMETERVALUE_INVALIDALIVEDAYS = 'InvalidParameterValue.InvalidAliveDays'

# Incorrect rule IP.
INVALIDPARAMETERVALUE_INVALIDAUTHCLIENTIP = 'InvalidParameterValue.InvalidAuthClientIp'

# Invalid scaling policy parameters.
INVALIDPARAMETERVALUE_INVALIDAUTOSCALEUPPARAMS = 'InvalidParameterValue.InvalidAutoScaleUpParams'

# The string used to ensure the idempotency of the request is incorrect.
INVALIDPARAMETERVALUE_INVALIDCLIENTTOKEN = 'InvalidParameterValue.InvalidClientToken'

# 
INVALIDPARAMETERVALUE_INVALIDDESTINATIONREGIONS = 'InvalidParameterValue.InvalidDestinationRegions'

# Invalid encryption parameter.
INVALIDPARAMETERVALUE_INVALIDENCRYPTED = 'InvalidParameterValue.InvalidEncrypted'

# `FileSystemId` is invalid.
INVALIDPARAMETERVALUE_INVALIDFILESYSTEMID = 'InvalidParameterValue.InvalidFileSystemId'

# Invalid custom name.
INVALIDPARAMETERVALUE_INVALIDFSNAME = 'InvalidParameterValue.InvalidFsName'

# Invalid file system quota.
INVALIDPARAMETERVALUE_INVALIDFSSIZELIMIT = 'InvalidParameterValue.InvalidFsSizeLimit'

# Invalid file system status.
INVALIDPARAMETERVALUE_INVALIDFSSTATUS = 'InvalidParameterValue.InvalidFsStatus'

# Incorrect mount target IP.
INVALIDPARAMETERVALUE_INVALIDMOUNTTARGETIP = 'InvalidParameterValue.InvalidMountTargetIp'

# Invalid network type.
INVALIDPARAMETERVALUE_INVALIDNETINTERFACE = 'InvalidParameterValue.InvalidNetInterface'

# Invalid value of `DayOfMonth`.
INVALIDPARAMETERVALUE_INVALIDPARAMDAYOFMONTH = 'InvalidParameterValue.InvalidParamDayOfMonth'

# 
INVALIDPARAMETERVALUE_INVALIDPARAMDAYOFWEEK = 'InvalidParameterValue.InvalidParamDayOfWeek'

# Invalid value of `IntervalDays`.
INVALIDPARAMETERVALUE_INVALIDPARAMINTERVALDAYS = 'InvalidParameterValue.InvalidParamIntervalDays'

# The permission group is not under this user.
INVALIDPARAMETERVALUE_INVALIDPGROUP = 'InvalidParameterValue.InvalidPgroup'

# Invalid permission group ID.
INVALIDPARAMETERVALUE_INVALIDPGROUPID = 'InvalidParameterValue.InvalidPgroupId'

# Invalid permission group name.
INVALIDPARAMETERVALUE_INVALIDPGROUPNAME = 'InvalidParameterValue.InvalidPgroupName'

# Incorrect priority settings.
INVALIDPARAMETERVALUE_INVALIDPRIORITY = 'InvalidParameterValue.InvalidPriority'

# Invalid protocol parameter.
INVALIDPARAMETERVALUE_INVALIDPROTOCOL = 'InvalidParameterValue.InvalidProtocol'

# Either `ZoneName` or `ZoneId, Region` must be selected.
INVALIDPARAMETERVALUE_INVALIDREGIONZONEINFO = 'InvalidParameterValue.InvalidRegionZoneInfo'

# Invalid parameter value: invalid resource tag value.
INVALIDPARAMETERVALUE_INVALIDRESOURCETAGS = 'InvalidParameterValue.InvalidResourceTags'

# Incorrect read/write permission settings.
INVALIDPARAMETERVALUE_INVALIDRWPERMISSION = 'InvalidParameterValue.InvalidRwPermission'

# Invalid target capacity.
INVALIDPARAMETERVALUE_INVALIDSCALEUPTARGETCAPACITY = 'InvalidParameterValue.InvalidScaleupTargetCapacity'

# 
INVALIDPARAMETERVALUE_INVALIDSNAPPOLICYSTATUS = 'InvalidParameterValue.InvalidSnapPolicyStatus'

# 
INVALIDPARAMETERVALUE_INVALIDSNAPSHOTNAME = 'InvalidParameterValue.InvalidSnapshotName'

# 
INVALIDPARAMETERVALUE_INVALIDSNAPSHOTPOLICYNAME = 'InvalidParameterValue.InvalidSnapshotPolicyName'

# The snapshot is invalid.
INVALIDPARAMETERVALUE_INVALIDSNAPSHOTSTATUS = 'InvalidParameterValue.InvalidSnapshotStatus'

# The resource pack does not exist or has been bound.
INVALIDPARAMETERVALUE_INVALIDSTORAGERESOURCEPKG = 'InvalidParameterValue.InvalidStorageResourcePkg'

# Invalid storage class parameter.
INVALIDPARAMETERVALUE_INVALIDSTORAGETYPE = 'InvalidParameterValue.InvalidStorageType'

# Invalid subnet ID.
INVALIDPARAMETERVALUE_INVALIDSUBNETID = 'InvalidParameterValue.InvalidSubnetId'

# The tag key cannot be empty.
INVALIDPARAMETERVALUE_INVALIDTAGKEY = 'InvalidParameterValue.InvalidTagKey'

# The tag value is empty or the character is invalid.
INVALIDPARAMETERVALUE_INVALIDTAGVALUE = 'InvalidParameterValue.InvalidTagValue'

# The capacity value is invalid.
INVALIDPARAMETERVALUE_INVALIDTURBOCAPACITY = 'InvalidParameterValue.InvalidTurboCapacity'

# Incorrect user permission settings.
INVALIDPARAMETERVALUE_INVALIDUSERPERMISSION = 'InvalidParameterValue.InvalidUserPermission'

# The specified VIP is unavailable.
INVALIDPARAMETERVALUE_INVALIDVIP = 'InvalidParameterValue.InvalidVip'

# Invalid VPCID.
INVALIDPARAMETERVALUE_INVALIDVPCID = 'InvalidParameterValue.InvalidVpcId'

# Invalid VPC parameter.
INVALIDPARAMETERVALUE_INVALIDVPCPARAMETER = 'InvalidParameterValue.InvalidVpcParameter'

# Invalid AZ.
INVALIDPARAMETERVALUE_INVALIDZONEID = 'InvalidParameterValue.InvalidZoneId'

# Invalid AZ or AZ ID.
INVALIDPARAMETERVALUE_INVALIDZONEORZONEID = 'InvalidParameterValue.InvalidZoneOrZoneId'

# `FileSystemId` is missing.
INVALIDPARAMETERVALUE_MISSINGFILESYSTEMID = 'InvalidParameterValue.MissingFileSystemId'

# Either `FileSystemId` or `Region` must be selected.
INVALIDPARAMETERVALUE_MISSINGFILESYSTEMIDORREGION = 'InvalidParameterValue.MissingFileSystemIdOrRegion'

# `FileSystem` is missing.
INVALIDPARAMETERVALUE_MISSINGFSPARAMETER = 'InvalidParameterValue.MissingFsParameter'

# Key ID or ARN is missing.
INVALIDPARAMETERVALUE_MISSINGKMSKEYID = 'InvalidParameterValue.MissingKmsKeyId'

# The permission group name and description cannot both be empty.
INVALIDPARAMETERVALUE_MISSINGNAMEORDESCINFO = 'InvalidParameterValue.MissingNameOrDescinfo'

# The permission group name cannot be empty.
INVALIDPARAMETERVALUE_MISSINGPGROUPNAME = 'InvalidParameterValue.MissingPgroupName'

# Snapshot policy parameters missing.
INVALIDPARAMETERVALUE_MISSINGPOLICYPARAM = 'InvalidParameterValue.MissingPolicyParam'

# 
INVALIDPARAMETERVALUE_MISSINGSNAPNAMEORALIVEDAY = 'InvalidParameterValue.MissingSnapNameOrAliveDay'

# No storage pack is bound to.
INVALIDPARAMETERVALUE_MISSINGSTORAGERESOURCEPKG = 'InvalidParameterValue.MissingStorageResourcePkg'

# `SUBNETID` and `UNSUBNETID` cannot both be empty.
INVALIDPARAMETERVALUE_MISSINGSUBNETIDORUNSUBNETID = 'InvalidParameterValue.MissingSubnetidOrUnsubnetid'

# A VPC parameter is missing.
INVALIDPARAMETERVALUE_MISSINGVPCPARAMETER = 'InvalidParameterValue.MissingVpcParameter'

# `VPCID` and `UNVPCID` cannot both be empty.
INVALIDPARAMETERVALUE_MISSINGVPCIDORUNVPCID = 'InvalidParameterValue.MissingVpcidOrUnvpcid'

# `ZoneID` is missing.
INVALIDPARAMETERVALUE_MISSINGZONEID = 'InvalidParameterValue.MissingZoneId'

# Either `Zone` or `Zone_id` must be selected.
INVALIDPARAMETERVALUE_MISSINGZONEORZONEID = 'InvalidParameterValue.MissingZoneOrZoneId'

# The length of the permission group description exceeds the limit (255 bytes).
INVALIDPARAMETERVALUE_PGROUPDESCINFOLIMITEXCEEDED = 'InvalidParameterValue.PgroupDescinfoLimitExceeded'

# The length of the permission group name exceeds the limit (64 bytes).
INVALIDPARAMETERVALUE_PGROUPNAMELIMITEXCEEDED = 'InvalidParameterValue.PgroupNameLimitExceeded'

# The permission group rule and permission group do not match.
INVALIDPARAMETERVALUE_RULENOTMATCHPGROUP = 'InvalidParameterValue.RuleNotMatchPgroup'

# 
INVALIDPARAMETERVALUE_SNAPSHOTNAMELIMITEXCEEDED = 'InvalidParameterValue.SnapshotNameLimitExceeded'

# 
INVALIDPARAMETERVALUE_SNAPSHOTPOLICYNAMELIMITEXCEEDED = 'InvalidParameterValue.SnapshotPolicyNameLimitExceeded'

# Invalid parameter value: the number of tag keys exceeds the upper limit (6).
INVALIDPARAMETERVALUE_TAGKEYFILTERLIMITEXCEEDED = 'InvalidParameterValue.TagKeyFilterLimitExceeded'

# The length of the tag key exceeds the upper limit of 127 bytes.
INVALIDPARAMETERVALUE_TAGKEYLIMITEXCEEDED = 'InvalidParameterValue.TagKeyLimitExceeded'

# The number of tag values exceeds the maximum (10).
INVALIDPARAMETERVALUE_TAGVALUEFILTERLIMITEXCEEDED = 'InvalidParameterValue.TagValueFilterLimitExceeded'

# The length of the tag value exceeds the upper limit of 255 bytes.
INVALIDPARAMETERVALUE_TAGVALUELIMITEXCEEDED = 'InvalidParameterValue.TagValueLimitExceeded'

# Services are unavailable in this AZ.
INVALIDPARAMETERVALUE_UNAVAILABLEREGION = 'InvalidParameterValue.UnavailableRegion'

# Services are unavailable in this region.
INVALIDPARAMETERVALUE_UNAVAILABLEZONE = 'InvalidParameterValue.UnavailableZone'

# `ZoneId` and `Region` do not match.
INVALIDPARAMETERVALUE_ZONEIDREGIONNOTMATCH = 'InvalidParameterValue.ZoneIdRegionNotMatch'

# Missing parameter.
MISSINGPARAMETER = 'MissingParameter'

# Operation denied.
OPERATIONDENIED = 'OperationDenied'

# The resource is in use.
RESOURCEINUSE = 'ResourceInUse'

# The number of file systems has reached the upper limit.
RESOURCEINSUFFICIENT_FILESYSTEMLIMITEXCEEDED = 'ResourceInsufficient.FileSystemLimitExceeded'

# The number of permission groups has reached the upper limit.
RESOURCEINSUFFICIENT_PGROUPNUMBERLIMITEXCEEDED = 'ResourceInsufficient.PgroupNumberLimitExceeded'

# Resources in the region have been sold out.
RESOURCEINSUFFICIENT_REGIONSOLDOUT = 'ResourceInsufficient.RegionSoldOut'

# The number of rules exceeds the upper limit.
RESOURCEINSUFFICIENT_RULELIMITEXCEEDED = 'ResourceInsufficient.RuleLimitExceeded'

# Snapshots are not supported because the file system is too large.
RESOURCEINSUFFICIENT_SNAPSHOTSIZELIMITEXCEEDED = 'ResourceInsufficient.SnapshotSizeLimitExceeded'

# There is no IP available in this subnet.
RESOURCEINSUFFICIENT_SUBNETIPALLOCCUPIED = 'ResourceInsufficient.SubnetIpAllOccupied'

# The quantity of the resource tags reached the upper limit.
RESOURCEINSUFFICIENT_TAGLIMITEXCEEDED = 'ResourceInsufficient.TagLimitExceeded'

# The tag quota is insufficient.
RESOURCEINSUFFICIENT_TAGQUOTASEXCEEDED = 'ResourceInsufficient.TagQuotasExceeded'

# The number of Turbo file systems with special capacity has reached the upper limit.
RESOURCEINSUFFICIENT_TURBOSPECIALCAPACITYFILESYSTEMCOUNTLIMIT = 'ResourceInsufficient.TurboSpecialCapacityFileSystemCountLimit'

# The resource does not exist.
RESOURCENOTFOUND = 'ResourceNotFound'

# The file system does not exist.
RESOURCENOTFOUND_FILESYSTEMNOTFOUND = 'ResourceNotFound.FileSystemNotFound'

# The file system does not exist.
RESOURCENOTFOUND_FSNOTEXIST = 'ResourceNotFound.FsNotExist'

# The mount target does not exist.
RESOURCENOTFOUND_MOUNTTARGETNOTFOUND = 'ResourceNotFound.MountTargetNotFound'

# The permission group does not exist.
RESOURCENOTFOUND_PGROUPNOTFOUND = 'ResourceNotFound.PgroupNotFound'

# The resource does not exist: The resource ID cannot be found.
RESOURCENOTFOUND_RESOURCEPACKAGENOTFOUND = 'ResourceNotFound.ResourcePackageNotFound'

# The permission rule does not exist.
RESOURCENOTFOUND_RULENOTFOUND = 'ResourceNotFound.RuleNotFound'

# The snapshot ID does not exist.
RESOURCENOTFOUND_SNAPSHOTNOTFOUND = 'ResourceNotFound.SnapshotNotFound'

# Unauthorized operation.
UNAUTHORIZEDOPERATION = 'UnauthorizedOperation'

# Unsupported operation.
UNSUPPORTEDOPERATION = 'UnsupportedOperation'

# This AZ does not support the basic network.
UNSUPPORTEDOPERATION_BASICNETINTERFACENOTSUPPORTED = 'UnsupportedOperation.BasicNetInterfaceNotSupported'

# The appid is not on the allowlist of the KMS (the KMS allowlist is currently enabled).
UNSUPPORTEDOPERATION_MISSINGKMSACCESSPERMISSION = 'UnsupportedOperation.MissingKmsAccessPermission'

# Your account is in arrears. Please top up and try again.
UNSUPPORTEDOPERATION_OUTOFSERVICE = 'UnsupportedOperation.OutOfService'

# The CFS role was not authorized.
UNSUPPORTEDOPERATION_UNAUTHORIZEDCFSQCSROLE = 'UnsupportedOperation.UnauthorizedCfsQcsRole'

# Unverified user.
UNSUPPORTEDOPERATION_UNVERIFIEDUSER = 'UnsupportedOperation.UnverifiedUser'
