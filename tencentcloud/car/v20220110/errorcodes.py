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

# Concurrency quota not requested or request timed out.
FAILEDOPERATION_LOCKTIMEOUT = 'FailedOperation.LockTimeout'

# Failed to find the path.
FAILEDOPERATION_PATHNOTFOUND = 'FailedOperation.PathNotFound'

# Processing timed out.
FAILEDOPERATION_PROCESSTIMEOUT = 'FailedOperation.ProcessTimeout'

# The request for the current `UserId` is being processed. Try again later.
FAILEDOPERATION_SLOWDOWN = 'FailedOperation.SlowDown'

# Internal error.
INTERNALERROR = 'InternalError'

# Parameter error.
INVALIDPARAMETER = 'InvalidParameter'

# JSON parsing error.
INVALIDPARAMETER_JSONPARSEERROR = 'InvalidParameter.JsonParseError'

# Invalid parameter value.
INVALIDPARAMETERVALUE = 'InvalidParameterValue'

# The number of roles in a **multi-person interaction** scenario exceeds the limit.
LIMITEXCEEDED_ROLE = 'LimitExceeded.Role'

# Operation denied.
OPERATIONDENIED = 'OperationDenied'

# No available concurrency quota.
RESOURCENOTFOUND_NOIDLE = 'ResourceNotFound.NoIdle'

# Unable to find the session.
RESOURCENOTFOUND_SESSIONNOTFOUND = 'ResourceNotFound.SessionNotFound'

# Failed to access the concurrency instance.
RESOURCEUNAVAILABLE_ACCESSFAILED = 'ResourceUnavailable.AccessFailed'

# The instance is being initialized.
RESOURCEUNAVAILABLE_INITIALIZATION = 'ResourceUnavailable.Initialization'

# The session is being terminated.
UNSUPPORTEDOPERATION_STOPPING = 'UnsupportedOperation.Stopping'
