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


# Error with CAM signature/authentication.
AUTHFAILURE = 'AuthFailure'

# Number of returned cloud disks has reached the limit and no more cloud disks can be returned.
INSUFFICIENTREFUNDQUOTA = 'InsufficientRefundQuota'

# Insufficient snapshot quota.
INSUFFICIENTSNAPSHOTQUOTA = 'InsufficientSnapshotQuota'

# Internal error.
INTERNALERROR = 'InternalError'

# Dependent component request failed. Please contact customer service.
INTERNALERROR_COMPONENTERROR = 'InternalError.ComponentError'

# Resource query failed.
INTERNALERROR_FAILQUERYRESOURCE = 'InternalError.FailQueryResource'

# The operation performed on the resource failed. For error message, see the "Message" field in error description. Try again later or contact customer service.
INTERNALERROR_RESOURCEOPFAILED = 'InternalError.ResourceOpFailed'

# Insufficient account balance
INVALIDACCOUNT_INSUFFICIENTBALANCE = 'InvalidAccount.InsufficientBalance'

# `AutoSnapshotPolicyId` entered does not exist.
INVALIDAUTOSNAPSHOTPOLICYID_NOTFOUND = 'InvalidAutoSnapshotPolicyId.NotFound'

# Cloud disk is already bound to scheduled snapshot policy.
INVALIDDISK_ALREADYBOUND = 'InvalidDisk.AlreadyBound'

# The cloud disk is busy. Try again later.
INVALIDDISK_BUSY = 'InvalidDisk.Busy'

# The cloud disk has expired.
INVALIDDISK_EXPIRE = 'InvalidDisk.Expire'

# Non-elastic cloud disks are not supported.
INVALIDDISK_NOTPORTABLE = 'InvalidDisk.NotPortable'

# The cloud disk does not support snapshot.
INVALIDDISK_NOTSUPPORTSNAPSHOT = 'InvalidDisk.NotSupportSnapshot'

# Indicates that the operation is not supported for the cloud disk.
INVALIDDISK_NOTSUPPORTED = 'InvalidDisk.NotSupported'

# A snapshot is being created for the cloud disk. Try again later.
INVALIDDISK_SNAPSHOTCREATING = 'InvalidDisk.SnapshotCreating'

# Invalid cloud disk type.
INVALIDDISK_TYPEERROR = 'InvalidDisk.TypeError'

# The ‘DiskId’ entered does not exist.
INVALIDDISKID_NOTFOUND = 'InvalidDiskId.NotFound'

# The specified Filter is not supported.
INVALIDFILTER = 'InvalidFilter'

# Cloud Virtual Machine does not support mounting cloud disk.
INVALIDINSTANCE_NOTSUPPORTED = 'InvalidInstance.NotSupported'

# The ‘InstanceId’ entered does not exist.
INVALIDINSTANCEID_NOTFOUND = 'InvalidInstanceId.NotFound'

# Incorrect parameter.
INVALIDPARAMETER = 'InvalidParameter'

# Currently configured cloud disk not supported in current region.
INVALIDPARAMETER_DISKCONFIGNOTSUPPORTED = 'InvalidParameter.DiskConfigNotSupported'

# The size of the cloud disk does not match the snapshot size.
INVALIDPARAMETER_DISKSIZENOTMATCH = 'InvalidParameter.DiskSizeNotMatch'

# The project ID does not exist.
INVALIDPARAMETER_PROJECTIDNOTEXIST = 'InvalidParameter.ProjectIdNotExist'

# You need to convert the snapshot into an image first.
INVALIDPARAMETER_SHOULDCONVERTSNAPSHOTTOIMAGE = 'InvalidParameter.ShouldConvertSnapshotToImage'

# Invalid parameter value.
INVALIDPARAMETERVALUE = 'InvalidParameterValue'

# Number of labels bound to cloud disk exceeds the limit.
INVALIDPARAMETERVALUE_BINDDISKLIMITEXCEEDED = 'InvalidParameterValue.BindDiskLimitExceeded'

# Number of parameter values exceeds the limit.
INVALIDPARAMETERVALUE_LIMITEXCEEDED = 'InvalidParameterValue.LimitExceeded'

# Indicates that the operation is not supported for the snapshot.
INVALIDSNAPSHOT_NOTSUPPORTED = 'InvalidSnapshot.NotSupported'

# The ‘SnapshotId’ entered does not exist.
INVALIDSNAPSHOTID_NOTFOUND = 'InvalidSnapshotId.NotFound'

# The number of scheduled snapshot policies has reached the upper limit.
LIMITEXCEEDED_AUTOSNAPSHOTPOLICYOUTOFQUOTA = 'LimitExceeded.AutoSnapshotPolicyOutOfQuota'

# Number of instances mounted to cloud disk exceeds the limit.
LIMITEXCEEDED_INSTANCEATTACHEDDISK = 'LimitExceeded.InstanceAttachedDisk'

# Missing parameter.
MISSINGPARAMETER = 'MissingParameter'

# The resource is busy. Try again later.
RESOURCEBUSY = 'ResourceBusy'

# The resource is in use.
RESOURCEINUSE = 'ResourceInUse'

# The specified snapshot is being replicated to the destination region.
RESOURCEINUSE_COPYSNAPSHOTCONFLICT = 'ResourceInUse.CopySnapshotConflict'

# The cloud disk is being migrated. Try again later.
RESOURCEINUSE_DISKMIGRATING = 'ResourceInUse.DiskMigrating'

# The cloud disk is being rolled back. Please try again later.
RESOURCEINUSE_DISKROLLBACKING = 'ResourceInUse.DiskRollbacking'

# Insufficient resources.
RESOURCEINSUFFICIENT = 'ResourceInsufficient'

# Quota insufficient.
RESOURCEINSUFFICIENT_OVERQUOTA = 'ResourceInsufficient.OverQuota'

# The number of returned cloud disks has reached the limit and no more cloud disks can be returned.
RESOURCEINSUFFICIENT_OVERREFUNDQUOTA = 'ResourceInsufficient.OverRefundQuota'

# The resource does not exist.
RESOURCENOTFOUND = 'ResourceNotFound'

# The resource is not found.
RESOURCENOTFOUND_NOTFOUND = 'ResourceNotFound.NotFound'

# The resource is unavailable.
RESOURCEUNAVAILABLE = 'ResourceUnavailable'

# The cloud disk has been mounted to another CVM.
RESOURCEUNAVAILABLE_ATTACHED = 'ResourceUnavailable.Attached'

# The snapshot chain of the cloud disk is too long, so snapshot creation is refused.
RESOURCEUNAVAILABLE_DISKSNAPSHOTCHAINTOOLARGE = 'ResourceUnavailable.DiskSnapshotChainTooLarge'

# The cloud disk has expired.
RESOURCEUNAVAILABLE_EXPIRE = 'ResourceUnavailable.Expire'

# The non-elastic cloud disk does not support this operation.
RESOURCEUNAVAILABLE_NOTPORTABLE = 'ResourceUnavailable.NotPortable'

# Cloud disks cannot be returned.
RESOURCEUNAVAILABLE_NOTSUPPORTREFUND = 'ResourceUnavailable.NotSupportRefund'

# The resource does not support this operation.
RESOURCEUNAVAILABLE_NOTSUPPORTED = 'ResourceUnavailable.NotSupported'

# The cloud disk has been repossessed.
RESOURCEUNAVAILABLE_REPEATREFUND = 'ResourceUnavailable.RepeatRefund'

# Unable to use: the snapshot is being created
RESOURCEUNAVAILABLE_SNAPSHOTCREATING = 'ResourceUnavailable.SnapshotCreating'

# Too many snapshots are being created in the entire network.
RESOURCEUNAVAILABLE_TOOMANYCREATINGSNAPSHOT = 'ResourceUnavailable.TooManyCreatingSnapshot'

# Incorrect cloud disk type. For example, a system disk cannot be mounted to CVM.
RESOURCEUNAVAILABLE_TYPEERROR = 'ResourceUnavailable.TypeError'

# 
RESOURCEUNAVAILABLE_ZONENOTMATCH = 'ResourceUnavailable.ZoneNotMatch'

# Order conflict.
TRADEDEALCONFLICT = 'TradeDealConflict'

# The operation is unauthorized.
UNAUTHORIZEDOPERATION = 'UnauthorizedOperation'

# Multi-factor authentication (MFA) has expired. Please try again.
UNAUTHORIZEDOPERATION_MFAEXPIRED = 'UnauthorizedOperation.MFAExpired'

# Payment failed as the account has not completed identity verification.
UNAUTHORIZEDOPERATION_NOTCERTIFICATION = 'UnauthorizedOperation.NotCertification'

# No payment permission.
UNAUTHORIZEDOPERATION_NOTHAVEPAYMENTRIGHT = 'UnauthorizedOperation.NotHavePaymentRight'

# The authorization role does not exist.
UNAUTHORIZEDOPERATION_ROLENOTEXISTS = 'UnauthorizedOperation.RoleNotExists'

# Unsupported operation
UNSUPPORTEDOPERATION = 'UnsupportedOperation'

# 
UNSUPPORTEDOPERATION_DETACHPOD = 'UnsupportedOperation.DetachPod'

# The disk is encrypted.
UNSUPPORTEDOPERATION_DISKENCRYPT = 'UnsupportedOperation.DiskEncrypt'

# Instance mounted on cloud disk not shut down.
UNSUPPORTEDOPERATION_INSTANCENOTSTOPPED = 'UnsupportedOperation.InstanceNotStopped'

# The snapshot is shared with others. Please cancel the sharing first.
UNSUPPORTEDOPERATION_SNAPHASSHARED = 'UnsupportedOperation.SnapHasShared'

# A custom snapshot was created for this snapshot. First delete the corresponding image. 
UNSUPPORTEDOPERATION_SNAPSHOTHASBINDEDIMAGE = 'UnsupportedOperation.SnapshotHasBindedImage'

# The snapshot does not support cross-region replication.
UNSUPPORTEDOPERATION_SNAPSHOTNOTSUPPORTCOPY = 'UnsupportedOperation.SnapshotNotSupportCopy'

# The resource does not support this operation in this status.
UNSUPPORTEDOPERATION_STATEERROR = 'UnsupportedOperation.StateError'
