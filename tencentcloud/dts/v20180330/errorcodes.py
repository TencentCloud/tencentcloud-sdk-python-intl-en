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


# The current user is not allowed to perform this operation as the authentication failed.
AUTHFAILURE_UNAUTHORIZEDOPERATIONERROR = 'AuthFailure.UnauthorizedOperationError'

# This operation is prohibited.
FAILEDOPERATION_NOTALLOWOPERATION = 'FailedOperation.NotAllowOperation'

# Failed to start the task.
FAILEDOPERATION_STARTJOBFAILED = 'FailedOperation.StartJobFailed'

# This operation cannot be performed due to status conflict.
FAILEDOPERATION_STATUSINCONFLICT = 'FailedOperation.StatusInConflict'

# An internal error occurred.
INTERNALERROR = 'InternalError'

# Failed to create the async task.
INTERNALERROR_ADDTASKERROR = 'InternalError.AddTaskError'

# Internal scheduling system error.
INTERNALERROR_CELERYERROR = 'InternalError.CeleryError'

# CGW system error.
INTERNALERROR_CGWSYSTEMERROR = 'InternalError.CgwSystemError'

# Failed to access the database on the DTS platform.
INTERNALERROR_DATABASEERROR = 'InternalError.DatabaseError'

# Migration tasks are in conflict.
INTERNALERROR_DUPLICATEJOB = 'InternalError.DuplicateJob'

# Locks are in conflict.
INTERNALERROR_LOCKERROR = 'InternalError.LockError'

# Communication protocol error.
INTERNALERROR_PROTOCOLERROR = 'InternalError.ProtocolError'

# Internal error.
INTERNALERROR_UNDEFINEDERROR = 'InternalError.UndefinedError'

# Unknown internal error.
INTERNALERROR_UNKNOWNERROR = 'InternalError.UnknownError'

# A parameter error occurred.
INVALIDPARAMETER = 'InvalidParameter'

# Parameter value error.
INVALIDPARAMETER_BIZINVALIDPARAMETERVALUEERROR = 'InvalidParameter.BizInvalidParameterValueError'

# The instance does not exist.
INVALIDPARAMETER_INSTANCENOTFOUND = 'InvalidParameter.InstanceNotFound'

# Incorrect parameter value.
INVALIDPARAMETERVALUE_INVALIDPARAMETERVALUE = 'InvalidParameterValue.InvalidParameterValue'

# The number of idle migration tasks exceeds the limit.
LIMITEXCEEDED_MAXUNUSEDJOBS = 'LimitExceeded.MaxUnusedJobs'

# Operation denied.
OPERATIONDENIED = 'OperationDenied'

# The operation was denied as the condition was not met.
OPERATIONDENIED_BIZOPERATIONDENIEDERROR = 'OperationDenied.BizOperationDeniedError'

# Task operation failure.
OPERATIONDENIED_JOBOPERATIONDENIEDERROR = 'OperationDenied.JobOperationDeniedError'

# DTS does not support the current migration type.
OPERATIONDENIED_MIGRATESERVICESUPPORTERROR = 'OperationDenied.MigrateServiceSupportError'

# This operation cannot be performed.
OPERATIONDENIED_OPERATIONDENIED = 'OperationDenied.OperationDenied'

# The resource does not exist.
RESOURCENOTFOUND = 'ResourceNotFound'

# Resource not found.
RESOURCENOTFOUND_BIZRESOURCENOTFOUNDERROR = 'ResourceNotFound.BizResourceNotFoundError'

# The migration task does not exist.
RESOURCENOTFOUND_JOBNOTEXIST = 'ResourceNotFound.JobNotExist'

# The instance is not found.
RESOURCENOTFOUND_RESOURCENOTFOUND = 'ResourceNotFound.ResourceNotFound'

# Verification failed. Insufficient permissions.
UNAUTHORIZEDOPERATION_NOTENOUGHPRIVILEGES = 'UnauthorizedOperation.NotEnoughPrivileges'

# Unsupported operation
UNSUPPORTEDOPERATION = 'UnsupportedOperation'
