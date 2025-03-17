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

# The current request is not authorized by CAM.
AUTHFAILURE_UNAUTHORIZEDOPERATION = 'AuthFailure.UnauthorizedOperation'

# Operation failed.
FAILEDOPERATION = 'FailedOperation'

# Failed to obtain tags.
FAILEDOPERATION_ACCESSTAGFAIL = 'FailedOperation.AccessTagFail'

# Failed to query database.
FAILEDOPERATION_DBQUERYFAILED = 'FailedOperation.DbQueryFailed'

# Failed to create database record.
FAILEDOPERATION_DBRECORDCREATEFAILED = 'FailedOperation.DbRecordCreateFailed'

# Failed to update database record.
FAILEDOPERATION_DBRECORDUPDATEFAILED = 'FailedOperation.DbRecordUpdateFailed'

# The job status is not running.
FAILEDOPERATION_JOBSTATUSNOTRUNNING = 'FailedOperation.JobStatusNotRunning'

# No task in the job.
FAILEDOPERATION_NOTASKSINJOB = 'FailedOperation.NoTasksInJob'

# The current environment does not support.
FAILEDOPERATION_NOTSUPPORTEDINENV = 'FailedOperation.NotSupportedInEnv'

# The resource does not exist.
FAILEDOPERATION_RESOURCENOTFOUND = 'FailedOperation.ResourceNotFound'

# Failed to send request.
FAILEDOPERATION_SENDREQUEST = 'FailedOperation.SendRequest'

# Internal error.
INTERNALERROR = 'InternalError'

# Invalid parameter.
INVALIDPARAMETER = 'InvalidParameter'

# Invalid parameter value.
INVALIDPARAMETERVALUE = 'InvalidParameterValue'

# The quota limit is exceeded.
LIMITEXCEEDED = 'LimitExceeded'

# Insufficient resources.
RESOURCEINSUFFICIENT = 'ResourceInsufficient'

# The resource does not exist.
RESOURCENOTFOUND = 'ResourceNotFound'

# Unauthorized operation.
UNAUTHORIZEDOPERATION = 'UnauthorizedOperation'
