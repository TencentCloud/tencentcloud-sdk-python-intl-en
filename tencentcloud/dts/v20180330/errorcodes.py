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

# A parameter error occurred.
INVALIDPARAMETER = 'InvalidParameter'

# The instance does not exist.
INVALIDPARAMETER_INSTANCENOTFOUND = 'InvalidParameter.InstanceNotFound'

# Incorrect parameter value.
INVALIDPARAMETERVALUE_INVALIDPARAMETERVALUE = 'InvalidParameterValue.InvalidParameterValue'

# The number of idle migration tasks exceeds the limit.
LIMITEXCEEDED_MAXUNUSEDJOBS = 'LimitExceeded.MaxUnusedJobs'

# Operation denied.
OPERATIONDENIED = 'OperationDenied'

# This operation cannot be performed.
OPERATIONDENIED_OPERATIONDENIED = 'OperationDenied.OperationDenied'

# The resource does not exist.
RESOURCENOTFOUND = 'ResourceNotFound'

# The migration task does not exist.
RESOURCENOTFOUND_JOBNOTEXIST = 'ResourceNotFound.JobNotExist'

# The instance is not found.
RESOURCENOTFOUND_RESOURCENOTFOUND = 'ResourceNotFound.ResourceNotFound'

# Verification failed. Insufficient permissions.
UNAUTHORIZEDOPERATION_NOTENOUGHPRIVILEGES = 'UnauthorizedOperation.NotEnoughPrivileges'

# Unsupported operation
UNSUPPORTEDOPERATION = 'UnsupportedOperation'

# The current instance type does not support this operation.
UNSUPPORTEDOPERATION_ACTIONNOTSUPPORT = 'UnsupportedOperation.ActionNotSupport'
