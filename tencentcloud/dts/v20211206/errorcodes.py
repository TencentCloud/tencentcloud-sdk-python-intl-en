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


# The CAM signature/authentication information is incorrect.
AUTHFAILURE = 'AuthFailure'

# Authentication failed.
AUTHFAILURE_AUTHFAILUREERROR = 'AuthFailure.AuthFailureError'

# Authentication was denied.
AUTHFAILURE_AUTHORIZEDOPERATIONDENYERROR = 'AuthFailure.AuthorizedOperationDenyError'

# The current user is not allowed to perform this operation as the authentication failed.
AUTHFAILURE_UNAUTHORIZEDOPERATIONERROR = 'AuthFailure.UnauthorizedOperationError'

# DryRun operation, which means an unnecessary DryRun parameter is passed in yet the request will still be successful.
DRYRUNOPERATION_DRYRUNOPERATIONERROR = 'DryRunOperation.DryRunOperationError'

# Operation failed.
FAILEDOPERATION = 'FailedOperation'

# The operation failed.
FAILEDOPERATION_FAILEDOPERATIONERROR = 'FailedOperation.FailedOperationError'

# This operation is prohibited.
FAILEDOPERATION_NOTALLOWOPERATION = 'FailedOperation.NotAllowOperation'

# Failed to start the task.
FAILEDOPERATION_STARTJOBFAILED = 'FailedOperation.StartJobFailed'

# This operation cannot be performed due to a status conflict.
FAILEDOPERATION_STATUSINCONFLICT = 'FailedOperation.StatusInConflict'

# 
FAILEDOPERATION_USERNOTAUTHED = 'FailedOperation.UserNotAuthed'

# An internal error occurred.
INTERNALERROR = 'InternalError'

# Failed to create the async task.
INTERNALERROR_ADDTASKERROR = 'InternalError.AddTaskError'

# An internal scheduling system error occurred.
INTERNALERROR_CELERYERROR = 'InternalError.CeleryError'

# A CGW system error occurred.
INTERNALERROR_CGWSYSTEMERROR = 'InternalError.CgwSystemError'

# Failed to access the database on the DTS platform.
INTERNALERROR_DATABASEERROR = 'InternalError.DatabaseError'

# Migration tasks are in conflict.
INTERNALERROR_DUPLICATEJOB = 'InternalError.DuplicateJob'

# HTTP request error.
INTERNALERROR_EXECHTTPREQUESTERROR = 'InternalError.ExecHttpRequestError'

# An internal error occurred.
INTERNALERROR_INTERNALERRORERROR = 'InternalError.InternalErrorError'

# An HTTP access request error occurred.
INTERNALERROR_INTERNALHTTPSERVERERROR = 'InternalError.InternalHttpServerError'

# An error occurred while accessing the internal component.
INTERNALERROR_INTERNALINNERCOMMONERROR = 'InternalError.InternalInnerCommonError'

# Failed to call the billing service.
INTERNALERROR_INTERNALTRADEERROR = 'InternalError.InternalTradeError'

# Locks are in conflict.
INTERNALERROR_LOCKERROR = 'InternalError.LockError'

# The account balance is insufficient.
INTERNALERROR_NOTENOUGHMONEYERROR = 'InternalError.NotEnoughMoneyError'

# A communication protocol error occurred.
INTERNALERROR_PROTOCOLERROR = 'InternalError.ProtocolError'

# An internal error occurred.
INTERNALERROR_UNDEFINEDERROR = 'InternalError.UndefinedError'

# An unknown internal error occurred.
INTERNALERROR_UNKNOWNERROR = 'InternalError.UnknownError'

# The parameter is incorrect.
INVALIDPARAMETER = 'InvalidParameter'

# The current API is not registered due to an exception.
INVALIDPARAMETER_CONTROLLERNOTFOUNDERROR = 'InvalidParameter.ControllerNotFoundError'

# The instance does not exist.
INVALIDPARAMETER_INSTANCENOTFOUND = 'InvalidParameter.InstanceNotFound'

# The parameter is invalid.
INVALIDPARAMETER_INVALIDPARAMETERERROR = 'InvalidParameter.InvalidParameterError'

# Invalid parameter value.
INVALIDPARAMETERVALUE = 'InvalidParameterValue'

# A data conversion error occurred.
INVALIDPARAMETERVALUE_DATACONVERTERROR = 'InvalidParameterValue.DataConvertError'

# The parameter value is incorrect.
INVALIDPARAMETERVALUE_INVALIDPARAMETERVALUE = 'InvalidParameterValue.InvalidParameterValue'

# The parameter is invalid.
INVALIDPARAMETERVALUE_INVALIDPARAMETERVALUEERROR = 'InvalidParameterValue.InvalidParameterValueError'

# The quantity exceeds the limit.
LIMITEXCEEDED_LIMITEXCEEDEDERROR = 'LimitExceeded.LimitExceededError'

# The number of idle migration tasks exceeds the limit.
LIMITEXCEEDED_MAXUNUSEDJOBS = 'LimitExceeded.MaxUnusedJobs'

# The parameter is missing.
MISSINGPARAMETER = 'MissingParameter'

# The parameter is lost.
MISSINGPARAMETER_MISSINGPARAMETERERROR = 'MissingParameter.MissingParameterError'

# The operation was denied.
OPERATIONDENIED = 'OperationDenied'

# The operation was denied as the condition was not met.
OPERATIONDENIED_BIZOPERATIONDENIEDERROR = 'OperationDenied.BizOperationDeniedError'

# The task operation failed.
OPERATIONDENIED_JOBOPERATIONDENIEDERROR = 'OperationDenied.JobOperationDeniedError'

# The account balance is insufficient.
OPERATIONDENIED_NOTENOUGHMONEYERROR = 'OperationDenied.NotEnoughMoneyError'

# This operation cannot be performed.
OPERATIONDENIED_OPERATIONDENIED = 'OperationDenied.OperationDenied'

# The operation was denied.
OPERATIONDENIED_OPERATIONDENIEDERROR = 'OperationDenied.OperationDeniedError'

# The number of requests exceeds the limit.
REQUESTLIMITEXCEEDED_REQUESTLIMITEXCEEDEDERROR = 'RequestLimitExceeded.RequestLimitExceededError'

# The resource is being used.
RESOURCEINUSE_RESOURCEINUSEERROR = 'ResourceInUse.ResourceInUseError'

# The resources are insufficient.
RESOURCEINSUFFICIENT_RESOURCEINSUFFICIENTERROR = 'ResourceInsufficient.ResourceInsufficientError'

# The resource does not exist.
RESOURCENOTFOUND = 'ResourceNotFound'

# The resource was not found.
RESOURCENOTFOUND_BIZRESOURCENOTFOUNDERROR = 'ResourceNotFound.BizResourceNotFoundError'

# The migration task does not exist.
RESOURCENOTFOUND_JOBNOTEXIST = 'ResourceNotFound.JobNotExist'

# The instance was not found.
RESOURCENOTFOUND_RESOURCENOTFOUND = 'ResourceNotFound.ResourceNotFound'

# The resource was not found.
RESOURCENOTFOUND_RESOURCENOTFOUNDERROR = 'ResourceNotFound.ResourceNotFoundError'

# The resource is unavailable.
RESOURCEUNAVAILABLE_RESOURCEUNAVAILABLEERROR = 'ResourceUnavailable.ResourceUnavailableError'

# The resources have been sold out.
RESOURCESSOLDOUT_RESOURCESSOLDOUTERROR = 'ResourcesSoldOut.ResourcesSoldOutError'

# The operation is unauthorized.
UNAUTHORIZEDOPERATION = 'UnauthorizedOperation'

# Authentication failed as there were no required permissions.
UNAUTHORIZEDOPERATION_NOTENOUGHPRIVILEGES = 'UnauthorizedOperation.NotEnoughPrivileges'

# The operation is unauthorized.
UNAUTHORIZEDOPERATION_PERMISSIONDENIED = 'UnauthorizedOperation.PermissionDenied'

# The operation is unauthorized.
UNAUTHORIZEDOPERATION_UNAUTHORIZEDOPERATIONERROR = 'UnauthorizedOperation.UnauthorizedOperationError'

# The parameter is unknown.
UNKNOWNPARAMETER = 'UnknownParameter'

# The parameter is unknown.
UNKNOWNPARAMETER_UNKNOWNPARAMETERERROR = 'UnknownParameter.UnknownParameterError'

# The operation is not supported.
UNSUPPORTEDOPERATION = 'UnsupportedOperation'

# The intranet user did not specify the required tags when creating the migration task. The **department**, **product**, and **owner** tags must be specified.
UNSUPPORTEDOPERATION_INTRANETUSERNOTTAGGEDERROR = 'UnsupportedOperation.IntraNetUserNotTaggedError'

# The intranet user did not specify the required tags when creating the sync task. The **department**, **product**, and **owner** tags must be specified.
UNSUPPORTEDOPERATION_INTRANETUSERNOTTAGGEDFORSYNCJOBERROR = 'UnsupportedOperation.IntraNetUserNotTaggedForSyncJobError'

# The operation is not supported.
UNSUPPORTEDOPERATION_UNSUPPORTEDOPERATIONERROR = 'UnsupportedOperation.UnsupportedOperationError'
