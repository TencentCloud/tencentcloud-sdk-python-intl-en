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


# CAM Signature/Authentication Error.
AUTHFAILURE = 'AuthFailure'

# Not logged in or login has expired.
AUTHFAILURE_SIGNATUREEXPIRE = 'AuthFailure.SignatureExpire'

# CAM not authorized, please contact the primary account to grant the QcloudWeDataFullAccess policy to this account.
AUTHFAILURE_UNAUTHORIZEDOPERATION = 'AuthFailure.UnauthorizedOperation'

# Dry Run Operation, indicating that the request would be successful, but the DryRun parameter was additionally passed.
DRYRUNOPERATION = 'DryRunOperation'

# Operation Failure.
FAILEDOPERATION = 'FailedOperation'

# Query data development resource lock status - Current user does not hold the lock
FAILEDOPERATION_NOLOCK = 'FailedOperation.NoLock'

# An internal error occurs.
INTERNALERROR = 'InternalError'

# External System Call Exception.
INTERNALERROR_CALLSCHEDULERAPIERROR = 'InternalError.CallSchedulerApiError'

# Failed to call TencentCloud API.
INTERNALERROR_INTERNALCALLCLOUDAPIERROR = 'InternalError.InternalCallCloudApiError'

# Parameter error.
INVALIDPARAMETER = 'InvalidParameter'

# Data Engine Instance does not exist.
INVALIDPARAMETER_DATAENGINEINSTANCENOTEXISTS = 'InvalidParameter.DataEngineInstanceNotExists'

# Duplicate Name.
INVALIDPARAMETER_DUPLICATENAME = 'InvalidParameter.DuplicateName'

# Incorrect Query Filter Parameter.
INVALIDPARAMETER_INVALIDFILTERPARAMETER = 'InvalidParameter.InvalidFilterParameter'

# Rule does not exist.
INVALIDPARAMETER_RULENOTEXIST = 'InvalidParameter.RuleNotExist'

# Rule Template does not exist.
INVALIDPARAMETER_RULETEMPLATENOTEXIST = 'InvalidParameter.RuleTemplateNotExist'

# Service Busy, please try again later.
INVALIDPARAMETER_SERVICEISBUSY = 'InvalidParameter.ServiceIsBusy'

# WeData_QCSRole does not exist, please authorize the service.
INVALIDPARAMETER_WEDATAROLENOTEXISTS = 'InvalidParameter.WeDataRoleNotExists'

# Workspace does not exist.
INVALIDPARAMETER_WORKSPACENOTEXIST = 'InvalidParameter.WorkspaceNotExist'

# Parameter value error.
INVALIDPARAMETERVALUE = 'InvalidParameterValue'

# Quota limit exceeded.
LIMITEXCEEDED = 'LimitExceeded'

# Missing Parameter Error.
MISSINGPARAMETER = 'MissingParameter'

# Operation Rejected.
OPERATIONDENIED = 'OperationDenied'

# The user is not in the allowlist.
OPERATIONDENIED_USERNOTINWHITELISTERROR = 'OperationDenied.UserNotInWhitelistError'

# The number of requests exceeded the frequency limit.
REQUESTLIMITEXCEEDED = 'RequestLimitExceeded'

# Resource Occupied.
RESOURCEINUSE = 'ResourceInUse'

# Insufficient resources.
RESOURCEINSUFFICIENT = 'ResourceInsufficient'

# The resource does not exist.
RESOURCENOTFOUND = 'ResourceNotFound'

# Resource Unavailable.
RESOURCEUNAVAILABLE = 'ResourceUnavailable'

# Resources sold out.
RESOURCESSOLDOUT = 'ResourcesSoldOut'

# Unauthorized Operation.
UNAUTHORIZEDOPERATION = 'UnauthorizedOperation'

# User is not a member of the current project.
UNAUTHORIZEDOPERATION_USERNOTINPROJECT = 'UnauthorizedOperation.UserNotInProject'

# Unknown parameter error.
UNKNOWNPARAMETER = 'UnknownParameter'

# Operation not supported.
UNSUPPORTEDOPERATION = 'UnsupportedOperation'

# Please configure at least one rule first.
UNSUPPORTEDOPERATION_NORULEINRULEGROUP = 'UnsupportedOperation.NoRuleInRuleGroup'
