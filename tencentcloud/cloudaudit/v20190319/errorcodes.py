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


# Operation failed.
FAILEDOPERATION = 'FailedOperation'

# Failed to check whether the CLS log topic exists
FAILEDOPERATION_CHECKCLSTOPICISEXISTFAILED = 'FailedOperation.CheckClsTopicIsExistFailed'

# Failed to check whether the COS bucket exists
FAILEDOPERATION_CHECKCOSBUCKETISEXISTFAILED = 'FailedOperation.CheckCosBucketIsExistFailed'

# Failed to create the COS bucket.
FAILEDOPERATION_CREATEBUCKETFAIL = 'FailedOperation.CreateBucketFail'

# Failed to pull the CLS log topic
FAILEDOPERATION_GETCLSTOPICFAILED = 'FailedOperation.GetClsTopicFailed'

# Failed to pull the COS bucket list
FAILEDOPERATION_GETCOSBUCKETLISTFAILED = 'FailedOperation.GetCosBucketListFailed'

# Internal error.
INTERNALERROR = 'InternalError'

# An exception occurred while creating the CMQ queue, probably because the CMQ queue to be created already exists, or your account has no permission or has overdue payments.
INTERNALERROR_CMQERROR = 'InternalError.CmqError'

# An error occurred while creating the tracking set. Submit a ticket for assistance.
INTERNALERROR_CREATEAUDITERROR = 'InternalError.CreateAuditError'

# Failed to delete the tracking set. Submit a ticket for assistance.
INTERNALERROR_DELETEAUDITERROR = 'InternalError.DeleteAuditError'

# An error occurred while querying tracking set details. Submit a ticket for assistance.
INTERNALERROR_DESCRIBEAUDITERROR = 'InternalError.DescribeAuditError'

# An error occurred while querying the number of tracking sets that can be created. Submit a ticket for assistance.
INTERNALERROR_INQUIREAUDITCREDITERROR = 'InternalError.InquireAuditCreditError'

# An internal error occurred while querying the summary of tracking sets. Submit a ticket for assistance.
INTERNALERROR_LISTAUDITSERROR = 'InternalError.ListAuditsError'

# An internal error occurred. Submit a ticket for assistance.
INTERNALERROR_LISTCMQENABLEREGIONERROR = 'InternalError.ListCmqEnableRegionError'

# An internal error occurred. Submit a ticket for assistance.
INTERNALERROR_LISTCOSENABLEREGIONERROR = 'InternalError.ListCosEnableRegionError'

# An internal error occurred. Submit a ticket for assistance.
INTERNALERROR_SEARCHERROR = 'InternalError.SearchError'

# An internal error occurred. Submit a ticket for assistance.
INTERNALERROR_STARTLOGGINGERROR = 'InternalError.StartLoggingError'

# An internal error occurred. Submit a ticket for assistance.
INTERNALERROR_STOPLOGGINGERROR = 'InternalError.StopLoggingError'

# An internal error occurred. Submit a ticket for assistance.
INTERNALERROR_UPDATEAUDITERROR = 'InternalError.UpdateAuditError'

# Parameter error.
INVALIDPARAMETER = 'InvalidParameter'

# The parameter must contain the start time and end time and must be an integer timestamp (accurate down to the second).
INVALIDPARAMETER_TIME = 'InvalidParameter.Time'

# The alias already exists.
INVALIDPARAMETERVALUE_ALIASALREADYEXISTS = 'InvalidParameterValue.AliasAlreadyExists'

# The tracking set name is non-compliant.
INVALIDPARAMETERVALUE_AUDITNAMEERROR = 'InvalidParameterValue.AuditNameError'

# The tracking set name cannot be modified.
INVALIDPARAMETERVALUE_AUDITTRACKNAMENOTSUPPORTMODIFY = 'InvalidParameterValue.AuditTrackNameNotSupportModify'

# CloudAudit currently does not support the entered CMQ region.
INVALIDPARAMETERVALUE_CMQREGIONERROR = 'InvalidParameterValue.CmqRegionError'

# The entered COS bucket name is non-compliant.
INVALIDPARAMETERVALUE_COSNAMEERROR = 'InvalidParameterValue.CosNameError'

# CloudAudit currently does not support the entered COS region.
INVALIDPARAMETERVALUE_COSREGIONERROR = 'InvalidParameterValue.CosRegionError'

# The value of `IsCreateNewBucket` can be 0 or 1. 0 indicates not to create a bucket, while 1 indicates to create a bucket.
INVALIDPARAMETERVALUE_ISCREATENEWBUCKETERROR = 'InvalidParameterValue.IsCreateNewBucketError'

# The value of `IsCreateNewQueue` can be 0 or 1. 0 indicates not to create a queue, while 1 indicates to create a queue.
INVALIDPARAMETERVALUE_ISCREATENEWQUEUEERROR = 'InvalidParameterValue.IsCreateNewQueueError'

# The value of `IsEnableCmqNotify` can be 0 or 1. 0 indicates not to enable CMQ delivery, while 1 indicates to enable CMQ delivery.
INVALIDPARAMETERVALUE_ISENABLECMQNOTIFYERROR = 'InvalidParameterValue.IsEnableCmqNotifyError'

# The log prefix format is incorrect.
INVALIDPARAMETERVALUE_LOGFILEPREFIXERROR = 'InvalidParameterValue.LogFilePrefixError'

# The maximum number of entries returned in one search is 50.
INVALIDPARAMETERVALUE_MAXRESULT = 'InvalidParameterValue.MaxResult'

# The entered queue name is non-compliant.
INVALIDPARAMETERVALUE_QUEUENAMEERROR = 'InvalidParameterValue.QueueNameError'

# Valid values of the read/write attribute: 1 (read-only), 2 (write-only), 3 (read/write).
INVALIDPARAMETERVALUE_READWRITEATTRIBUTEERROR = 'InvalidParameterValue.ReadWriteAttributeError'

# The start time cannot be after the end time.
INVALIDPARAMETERVALUE_TIME = 'InvalidParameterValue.Time'

# Valid values of `AttributeKey`: RequestId, EventName, ReadOnly, Username, ResourceType, ResourceName, AccessKeyId
INVALIDPARAMETERVALUE_ATTRIBUTEKEY = 'InvalidParameterValue.attributeKey'

# The maximum number of tracking sets has been exceeded.
LIMITEXCEEDED_OVERAMOUNT = 'LimitExceeded.OverAmount'

# Only entries for the last 7 days can be searched for.
LIMITEXCEEDED_OVERTIME = 'LimitExceeded.OverTime'

# The tracking set name is missing.
MISSINGPARAMETER_MISSAUDITNAME = 'MissingParameter.MissAuditName'

# The COS bucket parameter is missing.
MISSINGPARAMETER_MISSCOSBUCKETNAME = 'MissingParameter.MissCosBucketName'

# The COS region parameter is missing.
MISSINGPARAMETER_MISSCOSREGION = 'MissingParameter.MissCosRegion'

# If the value of `IsEnableCmqNotify` is 1, `IsCreateNewQueue`, `CmqQueueName`, and `CmqRegion` are required.
MISSINGPARAMETER_CMQ = 'MissingParameter.cmq'

# A tracking set with the same name already exists.
RESOURCEINUSE_ALREADYEXISTSSAMEAUDIT = 'ResourceInUse.AlreadyExistsSameAudit'

# A tracking set with the same CMQ delivery configuration already exists.
RESOURCEINUSE_ALREADYEXISTSSAMEAUDITCMQCONFIG = 'ResourceInUse.AlreadyExistsSameAuditCmqConfig'

# A tracking set with the same COS delivery configuration already exists.
RESOURCEINUSE_ALREADYEXISTSSAMEAUDITCOSCONFIG = 'ResourceInUse.AlreadyExistsSameAuditCosConfig'

# The COS bucket already exists.
RESOURCEINUSE_COSBUCKETEXISTS = 'ResourceInUse.CosBucketExists'

# The resource doesn’t exist.
RESOURCENOTFOUND = 'ResourceNotFound'

# The tracking set does not exist.
RESOURCENOTFOUND_AUDITNOTEXIST = 'ResourceNotFound.AuditNotExist'

# The role doesn’t exist.
RESOURCENOTFOUND_ROLENOTEXIST = 'ResourceNotFound.RoleNotExist'
