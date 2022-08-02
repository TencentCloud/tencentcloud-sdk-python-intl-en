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


# The operation failed.
FAILEDOPERATION = 'FailedOperation'

# Another request is being processed. Try again later.
FAILEDOPERATION_ANOTHERREQUESTPROCESSING = 'FailedOperation.AnotherRequestProcessing'

# The HTTP client request failed.
FAILEDOPERATION_HTTPCLIENTDOREQUESTFAILED = 'FailedOperation.HttpClientDoRequestFailed'

# An internal error occurred.
INTERNALERROR = 'InternalError'

# A database error occurred.
INTERNALERROR_DBERROR = 'InternalError.DBError'

# The parameter is incorrect.
INVALIDPARAMETER = 'InvalidParameter'

# The data engine name is invalid.
INVALIDPARAMETER_INVALIDDATAENGINENAME = 'InvalidParameter.InvalidDataEngineName'

# The fault tolerance policy is invalid.
INVALIDPARAMETER_INVALIDFAILURETOLERANCE = 'InvalidParameter.InvalidFailureTolerance'

# The CAM role arn is invalid.
INVALIDPARAMETER_INVALIDROLEARN = 'InvalidParameter.InvalidRoleArn'

# SQL parsing failed.
INVALIDPARAMETER_INVALIDSQL = 'InvalidParameter.InvalidSQL'

# The number of SQL statements does not meet the specification.
INVALIDPARAMETER_INVALIDSQLNUM = 'InvalidParameter.InvalidSQLNum'

# The `SparkAppParam` is invalid.
INVALIDPARAMETER_INVALIDSPARKAPPPARAM = 'InvalidParameter.InvalidSparkAppParam'

# The storage location is incorrect.
INVALIDPARAMETER_INVALIDSTORELOCATION = 'InvalidParameter.InvalidStoreLocation'

# The `taskid` is invalid.
INVALIDPARAMETER_INVALIDTASKID = 'InvalidParameter.InvalidTaskId'

# The task type is invalid.
INVALIDPARAMETER_INVALIDTASKTYPE = 'InvalidParameter.InvalidTaskType'

# The task has ended and cannot be canceled.
INVALIDPARAMETER_TASKALREADYFINISHED = 'InvalidParameter.TaskAlreadyFinished'

# The parameter value is incorrect.
INVALIDPARAMETERVALUE = 'InvalidParameterValue'

# The resource does not exist.
RESOURCENOTFOUND = 'ResourceNotFound'

# The result path was not found.
RESOURCENOTFOUND_RESULTOUTPUTPATHNOTFOUND = 'ResourceNotFound.ResultOutputPathNotFound'

# The resource is unavailable.
RESOURCEUNAVAILABLE = 'ResourceUnavailable'

# The account balance is insufficient to run the SQL task.
RESOURCEUNAVAILABLE_BALANCEINSUFFICIENT = 'ResourceUnavailable.BalanceInsufficient'

# The sub-user does not have permission to use the compute engine.
UNAUTHORIZEDOPERATION_USECOMPUTINGENGINE = 'UnauthorizedOperation.UseComputingEngine'
