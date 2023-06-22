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


# CAM signature/authentication error.
AUTHFAILURE = 'AuthFailure'

# The request would have succeeded, but the DryRun parameter was used.
DRYRUNOPERATION = 'DryRunOperation'

# Operation failed.
FAILEDOPERATION = 'FailedOperation'

# Room status error. The room has ended.
FAILEDOPERATION_CLASSENDED = 'FailedOperation.ClassEnded'

# Room status error. The room has expired.
FAILEDOPERATION_CLASSEXPIRED = 'FailedOperation.ClassExpired'

# Class status error. The class has already started.
FAILEDOPERATION_CLASSSTARTED = 'FailedOperation.ClassStarted'

# A class session cannot be longer than five hours.
FAILEDOPERATION_CLASSTOOLONG = 'FailedOperation.ClassTooLong'

# Image parameter error.
FAILEDOPERATION_IMAGEARGINVALID = 'FailedOperation.ImageArgInvalid'

# The user origin ID already exists.
FAILEDOPERATION_ORIGINIDEXISTS = 'FailedOperation.OriginIdExists'

# Request timed out.
FAILEDOPERATION_REQUESTTIMEDOUT = 'FailedOperation.RequestTimedOut'

# The class has not ended.
FAILEDOPERATION_ROOMNOTEND = 'FailedOperation.RoomNotEnd'

# Internal error.
INTERNALERROR = 'InternalError'

# Invalid parameter.
INVALIDPARAMETER = 'InvalidParameter'

# Prohibited content (pornographic, terrorist, politically sensitive) detected.
INVALIDPARAMETER_CONTENT = 'InvalidParameter.Content'

# Unable to access the CSS/JavaScript address.
INVALIDPARAMETER_CSSORJS = 'InvalidParameter.CssOrJs'

# The end time cannot be earlier than the current time.
INVALIDPARAMETER_ENDTIME = 'InvalidParameter.EndTime'

# The number of users in the group reached the limit.
INVALIDPARAMETER_GROUPMEMBEROVERLIMIT = 'InvalidParameter.GroupMemberOverLimit'

# Parameter error. The teacher and group members are not specified.
INVALIDPARAMETER_GROUPPARAMINVALID = 'InvalidParameter.GroupParamInvalid'

# The teacher cannot be a group member.
INVALIDPARAMETER_GROUPTEACHERNOTMEMBER = 'InvalidParameter.GroupTeacherNotMember'

# The teacher does not exist.
INVALIDPARAMETER_GROUPTEACHERSNOTEXIST = 'InvalidParameter.GroupTeachersNotExist'

# Group type error.
INVALIDPARAMETER_GROUPTYPEINVALID = 'InvalidParameter.GroupTypeInvalid'

# `SdkAppId` is incorrect.
INVALIDPARAMETER_SDKAPPID = 'InvalidParameter.SdkAppId'

# The start time cannot be earlier than the current time.
INVALIDPARAMETER_STARTTIME = 'InvalidParameter.StartTime'

# Invalid parameter value.
INVALIDPARAMETERVALUE = 'InvalidParameterValue'

# The quota limit is reached.
LIMITEXCEEDED = 'LimitExceeded'

# Missing parameter.
MISSINGPARAMETER = 'MissingParameter'

# Operation denied.
OPERATIONDENIED = 'OperationDenied'

# Too many requests.
REQUESTLIMITEXCEEDED = 'RequestLimitExceeded'

# The resource is occupied.
RESOURCEINUSE = 'ResourceInUse'

# Insufficient resource.
RESOURCEINSUFFICIENT = 'ResourceInsufficient'

# Insufficient storage space.
RESOURCEINSUFFICIENT_RECORD = 'ResourceInsufficient.Record'

# Failed to enter the class. Please check your resource usage in the console.
RESOURCEINSUFFICIENT_ROOM = 'ResourceInsufficient.Room'

# The resource doesn’t exist.
RESOURCENOTFOUND = 'ResourceNotFound'

# The file does not exist.
RESOURCENOTFOUND_DOCUMENT = 'ResourceNotFound.Document'

# The group does not exist.
RESOURCENOTFOUND_GROUPNOTEXIST = 'ResourceNotFound.GroupNotExist'

# The user ID does not exist.
RESOURCENOTFOUND_GROUPPARTUSERSNOTEXIST = 'ResourceNotFound.GroupPartUsersNotExist'

# The room does not exist.
RESOURCENOTFOUND_ROOM = 'ResourceNotFound.Room'

# The user does not exist.
RESOURCENOTFOUND_USER = 'ResourceNotFound.User'

# The resource is unavailable.
RESOURCEUNAVAILABLE = 'ResourceUnavailable'

# Getting room data. Please wait.
RESOURCEUNAVAILABLE_ROOMSTATISTICS = 'ResourceUnavailable.RoomStatistics'

# The resources have been sold out.
RESOURCESSOLDOUT = 'ResourcesSoldOut'

# Unauthorized operation.
UNAUTHORIZEDOPERATION = 'UnauthorizedOperation'

# Unknown parameter error.
UNKNOWNPARAMETER = 'UnknownParameter'

# Unsupported operation.
UNSUPPORTEDOPERATION = 'UnsupportedOperation'
